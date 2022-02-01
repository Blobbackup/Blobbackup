import datetime
import json
import os
import stat
import time
import sys
import logging
import fnmatch
import time
import chunker

from zstd import ZSTD_compress, ZSTD_uncompress, Error
from blobbackup.bounded_thread_pool_executor import BoundedThreadPoolExecutor
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from base64 import urlsafe_b64encode
from os.path import dirname, join, basename
from pathlib import Path
from blobbackup.models import (BLOBBACKUP_DIR, encrypt, decrypt,
                    DEFAULT_UPLOAD_SPEED_LIMIT, DEFAULT_UPLOAD_BLOB_SIZE,
                    DEFAULT_THREAD_COUNT, DEFAULT_COMPRESSION_LEVEL,
                    HASH_WINDOW_SIZE, CH_BUZHASH, CHUNK_MIN_EXP, CHUNK_MAX_EXP)

MAX_BLOB_SIZE_KB = 1024
MAX_BLOB_SIZE = MAX_BLOB_SIZE_KB * 1024
ZSTD_COMPRESSION_LEVEL = 3


class AlreadyInitialized(Exception):
    pass


class WindowsPathTooLong(Exception):
    pass


class CorruptSnapshot(Exception):
    pass


def compress(data, compression_level=ZSTD_COMPRESSION_LEVEL):
    return ZSTD_compress(data, compression_level)


def decompress(data):
    return ZSTD_uncompress(data)


def compress_encrypt(data, password, compression_level=ZSTD_COMPRESSION_LEVEL):
    return encrypt(compress(data, compression_level), password)


def decrypt_decompress(data, password):
    return decompress(decrypt(data, password))


def compress_encrypt_obj(data, password, compression_level):
    return compress_encrypt(
        json.dumps(data).encode(), password, compression_level)


def decrypt_decompress_obj(data, password):
    return json.loads(decrypt_decompress(data, password))


def can_backup(path):
    return (os.path.isfile(path) or os.path.isdir(path))


def generate_key(salt, password):
    return scrypt(password, salt, 32, N=2**14, r=8, p=1)


def pretty_bytes(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.2f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f %s%s" % (num, 'Y', suffix)


def get_paths(root_path, callback=print, abort_fn=None, logger=None):
    if abort_fn is None:
        abort_fn = lambda: False

    if logger is None:
        logger = logging.getLogger("test")

    paths = []
    skipped_paths = []
    size = [0]

    def add_path(path):
        paths.append(path)
        size[0] += os.path.getsize(path)
        callback(f"Scanning: {pretty_bytes(size[0])}")

    for root, dirs, files in os.walk(root_path):
        for d in dirs:
            path = join(root, d)
            logger.info(f"Scanning dir {os.path.basename(path)}")
            if abort_fn():
                logger.error("Stopping scan")
                return [], []
            add_path(path)
        for f in files:
            path = join(root, f)
            logger.info(f"Scanning file {os.path.basename(path)}")
            if not can_read_file(path):
                logger.error(f"Skipping file {os.path.basename(path)}")
                skipped_paths.append(path)
                continue
            if abort_fn():
                logger.error(f"Stopping scan")
                return [], []
            add_path(path)
    return paths, skipped_paths


def get_datetime_obj(datetime_string):
    return datetime.datetime.strptime(datetime_string, "%Y-%m-%d-%H-%M-%S")


def get_current_time_string():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def fn_matches(path, rules):
    for rule in rules:
        posix_path = Path(path).as_posix()
        if fnmatch.fnmatch(posix_path, rule):
            return True
    return False


def is_file_hidden(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


def can_read_file(path):
    try:
        with open(path, "rb") as f:
            _ = f.read(1)
    except (FileNotFoundError, PermissionError, OSError):
        return False
    return True


class Repo(object):
    def __init__(self,
                 backend,
                 callback=print,
                 thread_count=None,
                 blob_size_kb=None,
                 upload_speed_limit=None,
                 compression_level=None,
                 enable_variable=None,
                 follow_symlinks=None,
                 min_variable_exp=None,
                 max_variable_exp=None,
                 logger=None):
        if logger is None:
            logger = logging.getLogger("test")
        if thread_count is None:
            thread_count = DEFAULT_THREAD_COUNT
        if blob_size_kb is None:
            blob_size_kb = DEFAULT_UPLOAD_BLOB_SIZE
        if upload_speed_limit is None:
            upload_speed_limit = DEFAULT_UPLOAD_SPEED_LIMIT
        if compression_level is None:
            compression_level = DEFAULT_COMPRESSION_LEVEL
        if follow_symlinks is None:
            follow_symlinks = False
        if enable_variable is None:
            enable_variable = False
        if min_variable_exp is None:
            min_variable_exp = CHUNK_MIN_EXP
        if max_variable_exp is None:
            max_variable_exp = CHUNK_MAX_EXP
        self.backend = backend
        self.callback = callback
        self.thread_count = thread_count
        self.blob_size = blob_size_kb * 1024
        self.upload_speed_limit = upload_speed_limit
        self.compression_level = compression_level
        self.follow_symlinks = follow_symlinks
        self.enable_variable = enable_variable
        self.min_variable_exp = min_variable_exp
        self.max_variable_exp = max_variable_exp
        self.logger = logger
        self.backed_up_size = 0
        self.backup_start_time = None

        self.max_thread_queue_size = thread_count * 10
        self.cancel = False

        self.blob_set = None
        self.snapshot_ids = None

        self.logger.debug(
            f"Repo (threads={thread_count}, compression_level={compression_level}, blob={blob_size_kb}, kbs={upload_speed_limit})"
        )

    def init(self, password):
        self.logger.debug(f"Repo.init()")

        if self.is_initialized():
            raise AlreadyInitialized()

        self.backend.makedirs("snapshots")
        self.backend.makedirs("blobs")
        self.backend.makedirs("keys")

        salt, master_key = os.urandom(16), os.urandom(32)
        self.backend.write("keys/salt", salt)

        password_key = generate_key(salt, password)
        enc_master_key = compress_encrypt(master_key, password_key,
                                          self.compression_level)
        self.backend.write("keys/master", enc_master_key)

    def _get_master_key(self, password):
        self.logger.debug("Repo._get_master_key()")
        salt = self.backend.read("keys/salt")
        password_key = generate_key(salt, password)

        enc_master_key = self.backend.read("keys/master")
        master_key = decrypt_decompress(enc_master_key, password_key)

        return master_key

    def is_initialized(self):
        init_flag_exists = self.backend.exists("keys/master")
        return init_flag_exists

    def check_password(self, password):
        try:
            self._get_master_key(password)
            return True
        except ValueError:
            return False

    def get_snapshot_obj(self, password, snapshot_id=None):
        self.logger.debug(f"Repo.get_snapshot_obj(snapshot_id={snapshot_id})")
        if snapshot_id is None:
            return []
        master_key = self._get_master_key(password)
        snapshot_path = f"snapshots/{snapshot_id}"
        encrypted_snapshot_json = self.backend.read(snapshot_path)
        snapshot_obj = decrypt_decompress_obj(encrypted_snapshot_json,
                                              master_key)
        return snapshot_obj

    def get_snapshot_ids(self):
        self.logger.debug("Repo.get_snapshot_ids()")
        snapshot_paths = self.backend.ls("snapshots")
        snapshot_ids = []
        for snapshot_path in snapshot_paths:
            snapshot_id = basename(snapshot_path)
            snapshot_ids.append(snapshot_id)
        return snapshot_ids

    def _get_prefix_paths_single(self, selected_path):
        self.logger.debug(f"Repo._get_prefix_paths_single({selected_path})")
        prefix_paths = []
        current_dirname = dirname(selected_path)
        prev_dirname = None
        while True:
            prefix_paths.append(current_dirname)
            current_dirname = dirname(current_dirname)
            if current_dirname == prev_dirname:
                break
            prev_dirname = current_dirname
        return prefix_paths

    def _get_prefix_paths(self, selected_paths):
        self.logger.debug(f"Repo._get_prefix_paths({str(selected_paths)})")
        prefix_paths = set()
        for selected_path in selected_paths:
            prefix_paths.update(self._get_prefix_paths_single(selected_path))
        prefix_paths_list = list(prefix_paths)
        return prefix_paths_list

    def _gen_blobs_fixed(self, path):
        with open(path, "rb") as f:
            while True:
                blob = f.read(self.blob_size)
                if len(blob) == 0:
                    break
                yield blob

    def _gen_blobs_buz(self, path):
        params = (CH_BUZHASH, self.min_variable_exp, self.max_variable_exp,
                  (self.min_variable_exp + self.max_variable_exp) // 2,
                  HASH_WINDOW_SIZE)
        ch = chunker.get_chunker(*params, seed=0)
        with open(path, "rb") as f:
            chunks = ch.chunkify(f)
            for chunk in chunks:
                blob = chunk.tobytes()
                if len(blob) == 0:
                    break
                yield blob

    def _gen_blobs(self, path):
        if self.enable_variable:
            return self._gen_blobs_buz(path)
        else:
            return self._gen_blobs_fixed(path)

    def _get_blob_set(self):
        self.logger.debug("Repo._get_blob_set()")
        if self.cancel:
            return set()
        blob_set = set()
        for blob_path in self.backend.ls("blobs"):
            if self.cancel:
                return blob_set
            blob_set.add(basename(blob_path))
        return blob_set

    def _time_str_since_start(self):
        backup_duration = time.time() - self.backup_start_time
        time_str = str(datetime.timedelta(seconds=int(backup_duration)))
        return time_str

    def _save_snapshot(self, master_key, snapshot_obj, snapshot_id=None):
        self.logger.debug("Repo._save_snapshot()")
        encrypted_snapshot_json = compress_encrypt_obj(snapshot_obj,
                                                       master_key,
                                                       self.compression_level)
        if snapshot_id is None:
            snapshot_id = get_current_time_string()
        snapshot_path = f"snapshots/{snapshot_id}"
        self.backend.write(snapshot_path, encrypted_snapshot_json)

        return snapshot_id

    def _backup_blob(self, master_key, blob_hash, blob, path):
        self.logger.debug(
            f"Repo._backup_blob(blob={len(blob)} bytes, path={path})")
        speed = 8 * self.uploaded_size / (time.time() - self.backup_start_time)
        if self.upload_speed_limit is not 0:
            while speed / 1024 > self.upload_speed_limit:
                time.sleep(0.05)
                speed = 8 * self.uploaded_size / (time.time() -
                                                  self.backup_start_time)
        if self.cancel:
            return
        self.callback(
            f"{pretty_bytes(self.backed_up_size)} / {pretty_bytes(speed, suffix='bps')}"
        )
        encrypted_blob = compress_encrypt(blob, master_key,
                                          self.compression_level)
        blob_path = f"blobs/{blob_hash}"
        self.backend.write(blob_path, encrypted_blob)
        self.uploaded_size += len(encrypted_blob)

    def _add_dir_to_snapshot(self, snapshot_obj, path):
        self.logger.debug(f"Repo._add_dir_to_snapshot({path})")
        snapshot_obj.append({
            "type": "dir",
            "path": Path(path).as_posix(),
        })

    def _add_file_to_snapshot(self, master_key, salt, skipped_paths,
                              snapshot_obj, pool, blob_set, path):
        if self.cancel:
            return
        self.logger.debug(f"Repo._add_file_to_snapshot({path})")
        try:
            blobs = []
            for blob in self._gen_blobs(path):
                if self.cancel:
                    return
                self.backed_up_size += len(blob)
                blob_hash = sha256(salt + blob).hexdigest()
                blobs.append(blob_hash)
                if blob_hash in blob_set:
                    continue
                self._backup_blob(master_key, blob_hash, blob, path)
                blob_set.add(blob_hash)
            snapshot_obj.append({
                "type": "file",
                "path": Path(path).as_posix(),
                "blobs": blobs
            })
        except (FileNotFoundError, PermissionError, OSError) as error:
            self.logger.error(f"Skipping file {path}: {type(error).__name__}")
            skipped_paths.append(
                f"{Path(path).as_posix()}: {type(error).__name__}")

    def _get_partial_snapshot_obj(self, selected_paths):
        selected_dirs = [p for p in selected_paths if os.path.isdir(p)]
        paths = self._get_prefix_paths(selected_paths) + selected_dirs
        snapshot_obj = []
        for path in paths:
            self._add_dir_to_snapshot(snapshot_obj, path)
        return snapshot_obj

    def _init_backup(self, password, selected_paths):
        self.logger.debug(f"Repo._init_backup({str(selected_paths)})")
        self.backed_up_size = 0
        self.uploaded_size = 0
        self.backup_start_time = time.time()
        pool = BoundedThreadPoolExecutor(self.max_thread_queue_size,
                                         self.thread_count)
        snapshot_obj = self._get_partial_snapshot_obj(selected_paths)
        master_key = self._get_master_key(password)
        salt = self.backend.read("keys/salt")
        return snapshot_obj, [], pool, master_key, salt

    def _finish_pool(self, pool):
        self.logger.debug("Repo._finish_pool()")
        pool.shutdown()

    def _should_skip_path(self, path, skipped_paths, exclude_rules,
                          include_hidden):
        skip_reason = ""
        if not self.follow_symlinks and not can_backup(path):
            self.logger.error(f"Skipping symlink {path}")
            skip_reason = "Symlink"
        if fn_matches(path, exclude_rules):
            self.logger.debug(f"Skipped excluded path {path}")
            skip_reason = "Excluded path"
        if os.path.isfile(path) and (sys.platform == "win32"
                                     or sys.platform == "win64"):
            try:
                if not include_hidden and is_file_hidden(path):
                    self.logger.debug(f"Skipping hidden path {path}")
                    skip_reason = "Hidden path"
            except (FileNotFoundError, PermissionError, OSError) as error:
                self.logger.error(
                    f"Skipping file {path}: {type(error).__name__}")
                skip_reason = type(error).__name__
        skipped = skip_reason != ""
        if skipped:
            skipped_paths.append(f"{path}: {skip_reason}")
        return skipped

    def _backup_internal(self, snapshot_obj, skipped_paths, pool, master_key,
                         salt, selected_paths, exclude_rules, include_hidden,
                         blob_set):
        for selected_path in selected_paths:
            self.logger.info(f"Processing {selected_path}")
            if self._should_skip_path(selected_path, skipped_paths,
                                      exclude_rules, include_hidden):
                continue
            if os.path.isfile(selected_path):
                if self.cancel:
                    return
                pool.submit(self._add_file_to_snapshot, master_key, salt,
                            skipped_paths, snapshot_obj, pool, blob_set,
                            selected_path)
                continue
            for root, dirs, files in os.walk(selected_path):
                if self._should_skip_path(root, skipped_paths, exclude_rules,
                                          include_hidden):
                    continue
                for d in dirs:
                    if self.cancel:
                        return
                    path = os.path.join(root, d)
                    if self._should_skip_path(path, skipped_paths,
                                              exclude_rules, include_hidden):
                        continue
                    self._add_dir_to_snapshot(snapshot_obj, path)
                for f in files:
                    if self.cancel:
                        return
                    path = os.path.join(root, f)
                    if self._should_skip_path(path, skipped_paths,
                                              exclude_rules, include_hidden):
                        continue
                    pool.submit(self._add_file_to_snapshot, master_key, salt,
                                skipped_paths, snapshot_obj, pool, blob_set,
                                path)

    def backup(self,
               password,
               selected_paths,
               exclude_rules=None,
               include_hidden=False):
        if exclude_rules is None:
            exclude_rules = set()
        exclude_rules.add(f"{BLOBBACKUP_DIR}*")
        self.logger.info("----------------------------------------------")
        time.sleep(0.5)
        self.logger.info("Backup started")
        self.callback("Backing up")
        blob_set = self._get_blob_set()
        self.logger.info("Downloaded metadata")
        snapshot_obj, skipped_paths, pool, master_key, salt = self._init_backup(
            password, selected_paths)

        self._backup_internal(snapshot_obj, skipped_paths, pool, master_key,
                              salt, selected_paths, exclude_rules,
                              include_hidden, blob_set)

        self._finish_pool(pool)
        if self.cancel:
            self.logger.info("Stopping")
            return None, None
        self.logger.info(
            f"Processed {pretty_bytes(self.backed_up_size)} ({self.backed_up_size:,} bytes)"
        )
        self.logger.info(
            f"Uploaded {pretty_bytes(self.uploaded_size)} ({self.uploaded_size:,} bytes)"
        )
        snapshot_id = self._save_snapshot(master_key, snapshot_obj)
        self.logger.info(f"Saved snapshot {snapshot_id}")
        self.blob_set = blob_set
        return snapshot_id, skipped_paths

    def _makedirs_if_not_exists(self, path):
        self.logger.debug(f"Repo._makedirs_if_not_exists({path})")
        if not os.path.exists(path):
            os.makedirs(path)

    def _restore_file(self, master_key, restore_path, blobs):
        self.logger.debug(
            f"Repo._restore_file(restore_path={restore_path}, blobs={len(blobs)} blobs)"
        )
        try:
            with open(restore_path, "wb") as f:
                for blob_hash in blobs:
                    if self.error is not None:
                        return
                    blob_path = f"blobs/{blob_hash}"
                    encrypted_blob = self.backend.read(blob_path)
                    blob = decrypt_decompress(encrypted_blob, master_key)
                    self.backed_up_size += len(blob)
                    self.callback(
                        f"Restoring: {pretty_bytes(self.backed_up_size)} / {self._time_str_since_start()}"
                    )
                    f.write(blob)
        except (FileNotFoundError, ValueError, Error) as error:
            if len(restore_path) > 260:
                error = WindowsPathTooLong(f"Path too long {restore_path}")
            self.logger.error(
                f"Skipping file {Path(restore_path).as_posix()}: {type(error).__name__}"
            )
        except Exception as error:
            self.logger.error(
                f"Skipping file {Path(restore_path).as_posix()}: {type(error).__name__}"
            )
            self.error = error

    def _init_restore(self, password, snapshot_id):
        self.backed_up_size = 0
        self.backup_start_time = time.time()
        self.error = None
        snapshot_obj = self.get_snapshot_obj(password, snapshot_id)
        master_key = self._get_master_key(password)
        pool = BoundedThreadPoolExecutor(self.thread_count,
                                         self.max_thread_queue_size)
        return snapshot_obj, pool, master_key

    def restore(self, password, snapshot_id, restore_dir, restore_paths=None):
        self.logger.info("----------------------------------------------")
        time.sleep(0.5)
        self.logger.info(f"Restore started {snapshot_id}")
        self.callback("Restoring")
        snapshot_obj, pool, master_key = self._init_restore(
            password, snapshot_id)
        self.logger.info("Downloaded metadata")
        for node in snapshot_obj:
            if self.error is not None:
                self.logger.info("Stopping")
                break
            path = node["path"]
            if restore_paths is not None and path not in restore_paths:
                continue
            if path[0] != "/":
                drive, remainder = path.split(":")[0], path.split(":")[1][1:]
                restore_path = join(restore_dir, drive, remainder)
            else:
                restore_path = join(restore_dir, path[1:])
            if node["type"] == "dir":
                self._makedirs_if_not_exists(restore_path)
            elif node["type"] == "file":
                self._makedirs_if_not_exists(dirname(restore_path))
                pool.submit(self._restore_file, master_key, restore_path,
                            node["blobs"])
        self._finish_pool(pool)
        self.logger.info(
            f"Restored {pretty_bytes(self.backed_up_size)} ({self.backed_up_size:,} bytes)"
        )
        if self.error is not None:
            raise self.error
        self.logger.info(f"Restore complete in {self._time_str_since_start()}")

    def _ref_count_snapshot_nodes(self, ref_count, snapshot_obj):
        self.logger.debug("Repo._ref_count_snapshot_nodes()")
        for node in snapshot_obj:
            if node["type"] == "file":
                for blob_hash in node["blobs"]:
                    ref_count[blob_hash] += 1

    def _rm_blob(self, blob_path, deleted):
        if self.cancel:
            return
        self.logger.debug(f"Repo._rm_blob({blob_path})")
        self.callback(f"Pruning: {deleted:,} old blobs")
        self.backend.rm(blob_path)

    def _prune_using_ref_count(self, ref_count):
        self.logger.debug("Repo._prune_using_ref_count()")
        pool = BoundedThreadPoolExecutor(self.max_thread_queue_size,
                                         self.thread_count)
        deleted = 0
        for blob_hash, count in ref_count.items():
            if self.cancel:
                return None
            if count is 0:
                deleted += 1
                blob_path = f"blobs/{blob_hash}"
                pool.submit(self._rm_blob, blob_path, deleted)
        self._finish_pool(pool)
        return deleted

    def prune(self, password):
        if self.backup_start_time is None:
            self.backup_start_time = time.time()
        self.logger.info("Prune started")
        if self.cancel:
            self.logger.info("Stopping")
            return None
        self.callback("Fetching metadata")
        self.snapshot_ids = self.get_snapshot_ids(
        ) if self.snapshot_ids is None else self.snapshot_ids
        blob_hashes = self._get_blob_set(
        ) if self.blob_set is None else self.blob_set
        self.logger.info("Downloaded metadata")
        ref_count = {}
        for blob_hash in blob_hashes:
            ref_count[blob_hash] = 0
        for snapshot_id in self.snapshot_ids:
            if self.cancel:
                self.logger.info("Stopping")
                return None
            self.callback(f"Checking: {snapshot_id}")
            self.logger.debug(f"Pruning {snapshot_id}")
            snapshot_obj = self.get_snapshot_obj(password, snapshot_id)
            try:
                self._ref_count_snapshot_nodes(ref_count, snapshot_obj)
            except KeyError:
                self.logger.error(f"Corrupted snapshot {snapshot_id}")
                raise CorruptSnapshot(snapshot_id)
        deleted = self._prune_using_ref_count(ref_count)
        self.logger.info(f"Pruned {deleted:,} blobs")
        self.logger.info(f"Backup complete in {self._time_str_since_start()}")
        return deleted

    def delete(self, snapshot_id):
        self.callback(f"Removing: {snapshot_id}")
        self.logger.debug(f"Repo.delete({snapshot_id})")
        snapshot_path = f"snapshots/{snapshot_id}"
        self.backend.rm(snapshot_path)

    def keep(self, retention):
        if self.cancel:
            return
        self.logger.debug(f"Repo.keep({retention} days)")
        current_datetime = datetime.datetime.now()
        self.snapshot_ids = self.get_snapshot_ids(
        ) if self.snapshot_ids is None else self.snapshot_ids
        pool = BoundedThreadPoolExecutor(self.max_thread_queue_size,
                                         self.thread_count)
        for snapshot_id in self.snapshot_ids:
            snapshot_datetime = get_datetime_obj(snapshot_id)
            days_since = (current_datetime - snapshot_datetime).days
            if days_since > retention:
                pool.submit(self.delete, snapshot_id)
        self._finish_pool(pool)

    def delete_file_from_snapshot(self, password, snapshot_id, paths):
        self.logger.debug(
            f"Repo.delete_file_from_snapshot(snapshot_id={snapshot_id}, paths={str(paths)})"
        )
        snapshot_obj = self.get_snapshot_obj(password, snapshot_id)
        to_delete_indices = []
        for i, node in enumerate(snapshot_obj):
            if node["path"] in paths:
                to_delete_indices.append(i)
        offset = 0
        for i in to_delete_indices:
            self.callback(f"Deleting {offset:,} files")
            del snapshot_obj[i - offset]
            offset += 1
        master_key = self._get_master_key(password)
        self._save_snapshot(master_key, snapshot_obj, snapshot_id)

    def delete_file(self, password, paths):
        self.snapshot_ids = self.get_snapshot_ids(
        ) if self.snapshot_ids is None else self.snapshot_ids
        for snapshot_id in self.snapshot_ids:
            self.delete_file_from_snapshot(password, snapshot_id, paths)
