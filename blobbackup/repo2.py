import os
import sys
import io
import chunker
import zstd
import json
import subprocess
import hashlib
import hmac
import datetime
import argparse
import getpass
import fnmatch
import time
import logging

from threading import BoundedSemaphore, Lock
from concurrent.futures import ThreadPoolExecutor
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from pathlib import Path
from functools import lru_cache
from blobbackup.models import BLOBBACKUP_DIR


class CorruptSnapshot(Exception):
    pass


class ConcatBytesIO(object):
    """
    We want the chunker to treat all the files in our 
    source as one long stream of bytes to avoid getting
    lots of small chunks to upload. This class provides 
    an interface for reading a list of `paths` as though
    it were one long file with the contents of each 
    individual file concatenated.
    """
    def __init__(self, paths, file_finished_callback, logger):
        """
        :param paths: iterator of file paths
        :param file_finished_callback: function to call when a 
            file has been read all the way through. Expect
            to receive arguments (file_path, offset)
        """
        self.paths = paths
        self.file_finished_callback = file_finished_callback
        self.logger = logger
        self.path = None
        self.file = None
        self.consumed = 0
        self.done = False

    def __del__(self):
        if self.file is not None:
            self.file.close()

    def read(self, n):
        """ 
        Collect bytes from the paths iterator until we have 
        enough to return. Will return whatever it can if 
        there aren't sufficient bytes in the stream.
        :param n: the number of bytes to read.
        """
        buffer = io.BytesIO()
        to_read = n
        while to_read > 0 and not self.done:
            read_bytes = b""
            if self.file is not None:
                read_bytes = self.file.read(to_read)
            if len(read_bytes) is 0:
                if self.file is not None:
                    self.file_finished_callback(self.path, self.consumed)
                try:
                    self.path = next(self.paths)
                except StopIteration:
                    self.done = True
                    break
                if self.file is not None:
                    self.file.close()
                try:
                    self.file = open(self.path, "rb")
                except (IOError, PermissionError):
                    self.file = None
                    self.logger.error(f"Skipped path {self.path}")
                continue
            buffer.write(read_bytes)
            self.consumed += len(read_bytes)
            to_read -= len(read_bytes)
        buffer.seek(0)
        return buffer.read()


CHUNKER_ALGORITHM = "buzhash"
CHUNKER_MIN_LOG = 20
CHUNKER_MAX_LOG = 24
CHUNKER_MASK_LOG = 22
CHUNKER_HASH_WINDOW = 0xfff
CHUNKER_SEED = 0


class ChunkMaker(object):
    """
    We need to know what files are contained in each chunk
    and where they are contained. This class uses the 
    ConcatBytesIO class and the chunking algorithm to 
    allow for sequential reading of chunks and the files 
    within them.
    """
    def __init__(self, paths, logger, start_chunk_idx=0):
        """
        :param paths: iterator of file paths
        :param start_chunk_idx: the starting point for chunk
            idxs. If we're just adding onto chunks from an
            existing snapshot, we can't simply start at 0.
        """
        self.paths = paths
        self.chunk_idx = start_chunk_idx
        self.concat_bytes_io = ConcatBytesIO(self.paths, self._processed,
                                             logger)
        self.chunks = chunker.get_chunker(CHUNKER_ALGORITHM,
                                          CHUNKER_MIN_LOG,
                                          CHUNKER_MAX_LOG,
                                          CHUNKER_MASK_LOG,
                                          CHUNKER_HASH_WINDOW,
                                          seed=CHUNKER_SEED).chunkify(
                                              self.concat_bytes_io)
        self.processed_paths = []
        self.next_chunk = b""
        self.consumed = 0
        self.prev_chunk_idx = start_chunk_idx
        self.prev_chunk_offset = 0

    def advance(self):
        """
        Populate the next_chunk buffer with the next chunk
        and update any counters. Returns empty bytes if 
        there are no more files to get chunks from.
        """
        try:
            self.next_chunk = next(self.chunks).tobytes()
            self.consumed += len(self.next_chunk)
            self.chunk_idx += 1
        except StopIteration:
            self.next_chunk = b""

    def get_chunk(self):
        """
        Get (next_chunk, chunk_paths) where chunk_paths is a 
        list of tuples of the form
        (path, (start_idx, start_offset, end_idx, end_offset))
        """
        chunk_paths = []
        while len(self.processed_paths) > 0:
            path, offset = self.processed_paths[0]
            if offset > self.consumed:
                break
            self.processed_paths.pop(0)
            start, end = self.prev_chunk_idx, self.chunk_idx - 1
            ostart = self.prev_chunk_offset
            oend = len(self.next_chunk) - (self.consumed - offset)
            chunk_paths.append((path, (start, ostart, end, oend)))
            self.prev_chunk_idx, self.prev_chunk_offset = end, oend
        return self.next_chunk, chunk_paths

    def _processed(self, path, offset):
        self.processed_paths.append((path, offset))


ZSTD_COMPRESSION_LEVEL = 3


def compress(data, compression_level=ZSTD_COMPRESSION_LEVEL):
    return zstd.ZSTD_compress(data, compression_level)


def decompress(data):
    return zstd.ZSTD_uncompress(data)


def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    cipher_text, mac = cipher.encrypt_and_digest(data)
    return cipher.nonce + cipher_text + mac


def decrypt(data, key):
    nonce, cipher_text, mac = data[:16], data[16:-16], data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(cipher_text, mac)


def compress_encrypt(data, password, compression_level=ZSTD_COMPRESSION_LEVEL):
    return encrypt(compress(data, compression_level), password)


def decrypt_decompress(data, password):
    return decompress(decrypt(data, password))


def compress_encrypt_obj(data,
                         password,
                         compression_level=ZSTD_COMPRESSION_LEVEL):
    return compress_encrypt(
        json.dumps(data).encode(), password, compression_level)


def decrypt_decompress_obj(data, password):
    return json.loads(decrypt_decompress(data, password))


def generate_key(salt, password):
    return scrypt(password, salt, 32, N=2**14, r=8, p=1)


def get_current_time_string():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def get_datetime_obj(datetime_string):
    return datetime.datetime.strptime(datetime_string, "%Y-%m-%d-%H-%M-%S")


def pretty_bytes(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.2f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f %s%s" % (num, 'Y', suffix)


def fn_matches(path, rules):
    for rule in rules:
        posix_path = Path(path).as_posix()
        if fnmatch.fnmatch(posix_path, rule):
            return True
    return False


DEFAULT_THREAD_COUNT = 4
DEFAULT_THREAD_BOUND = DEFAULT_THREAD_COUNT * 10


class BoundedThreadPoolExecutor(object):
    """
    The default python ThreadPoolExecutor lets its queue 
    get infinitely long. This can use excessive memory without
    any performance benefit. This class bounds the thread queue
    and only adds more items when needed. 
    Credit: https://www.bettercodebytes.com/theadpoolexecutor-with-a-bounded-queue-in-python/
    """
    def __init__(self, bound, max_workers):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.semaphore = BoundedSemaphore(bound + max_workers)

    def future_done(self, future):
        self.semaphore.release()
        exception = future.exception()
        if exception is not None:
            raise exception

    def submit(self, fn, *args, **kwargs):
        self.semaphore.acquire()
        try:
            future = self.executor.submit(fn, *args, **kwargs)
        except ValueError:
            self.semaphore.release()
            raise
        else:
            future.add_done_callback(lambda x: self.future_done(future))
            return future

    def shutdown(self, wait=True):
        self.executor.shutdown(wait)


class Repo(object):
    def __init__(self,
                 backend,
                 callback=print,
                 thread_count=None,
                 compression_level=None,
                 logger=None):
        if logger is None:
            logger = logging.getLogger("test")
        if thread_count is None:
            thread_count = DEFAULT_THREAD_COUNT
        if compression_level is None:
            compression_level = ZSTD_COMPRESSION_LEVEL
        self.backend = backend
        self.callback = callback
        self.thread_count = thread_count
        self.compression_level = compression_level
        self.logger = logger
        self.max_thread_queue_size = thread_count * 10
        self.cancel = False
        self.backup_start_time = None
        self.logger.debug(
            f"Repo (threads={thread_count}, compression_level={compression_level})"
        )

    def is_initialized(self):
        return self.backend.exists("keys/master-key")

    def check_password(self, password):
        try:
            self._get_master_key(password)
            return True
        except ValueError:
            return False

    def get_snapshot_obj(self, password, snapshot_id=None):
        self.logger.debug(f"Repo.get_snapshot_obj(snapshot_id={snapshot_id})")
        master_key = self._get_master_key(password)
        snapshot_path = f"snapshots/{snapshot_id}"
        encrypted_snapshot_json = self.backend.read(snapshot_path)
        snapshot_obj = decrypt_decompress_obj(encrypted_snapshot_json,
                                              master_key)
        return snapshot_obj

    def init(self, password):
        self.logger.debug(f"Repo.init()")

        self.backend.makedirs("keys")
        self.backend.makedirs("snapshots")
        self.backend.makedirs("chunks")

        salt, master, sha = os.urandom(16), os.urandom(32), os.urandom(32)
        key = generate_key(salt, password)
        self.backend.write("keys/key-salt", salt)
        self.backend.write("keys/master-key", encrypt(master, key))
        self.backend.write("keys/sha-key", encrypt(sha, master))

    def backup(self,
               password,
               include_paths,
               exclude_rules=None,
               include_hidden=False):
        if exclude_rules is None:
            exclude_rules = set()
        exclude_rules.add(f"{BLOBBACKUP_DIR}*")
        self.backup_start_time = time.time()

        self.logger.info("----------------------------------------------")
        self.logger.info("Backup started")
        self.callback("Backing up")

        master = self._get_master_key(password)
        sha = decrypt(self.backend.read("keys/sha-key"), master)

        snapshot = {}
        self.write_size = 0
        self.processed_size = 0
        self.write_size_lock = Lock()

        prev_snapshot, chunks = self._get_prev_snapshot(master)
        pool = BoundedThreadPoolExecutor(self.max_thread_queue_size,
                                         self.thread_count)
        chunk_maker = ChunkMaker(self._gen_paths_and_populate(
            include_paths, prev_snapshot, snapshot, exclude_rules),
                                 logger=self.logger,
                                 start_chunk_idx=len(chunks))
        self.logger.info("Downloaded metadata")

        while True:
            if self.cancel:
                self.logger.info("Stopping")
                break
            chunk_maker.advance()
            chunk, paths = chunk_maker.get_chunk()
            if len(chunk) is 0:
                break
            chunk_hash = hmac.new(sha, chunk, hashlib.sha256).hexdigest()
            chunk_path = f"chunks/{chunk_hash}"
            pool.submit(self._backup_chunk, chunk_path, chunk, master)
            chunks.append(chunk_hash)
            for args in paths:
                self._add_file_to_snapshot(snapshot, *args)
        pool.shutdown()

        if self.cancel:
            return None, None

        snapshot_obj = {
            "data_format_version": 1,
            "snapshot": snapshot,
            "chunks": chunks
        }

        self.logger.info(
            f"Processed {pretty_bytes(self.processed_size)} ({self.processed_size:,} bytes)"
        )
        self.logger.info(
            f"Wrote {pretty_bytes(self.write_size)} ({self.write_size:,} bytes)"
        )

        snapshot_id = get_current_time_string()
        snapshot_path = f"snapshots/{snapshot_id}"
        self.backend.write(
            snapshot_path,
            compress_encrypt_obj(snapshot_obj, master, self.compression_level))

        self.logger.info(f"Saved snapshot {snapshot_id}")

        return snapshot_id, []

    def restore(self, password, snapshot_id, restore_dir, restore_paths=None):
        self.logger.info("----------------------------------------------")
        self.logger.info(f"Restore started {snapshot_id}")
        self.callback("Restoring")

        self.backup_start_time = time.time()
        master = self._get_master_key(password)
        snapshot_obj = decrypt_decompress_obj(
            self.backend.read(f"snapshots/{snapshot_id}"), master)
        snapshot, chunks = snapshot_obj["snapshot"], snapshot_obj["chunks"]
        write_size = 0

        self.logger.info(f"Processing snapshot {snapshot_id}")
        self.logger.info("Downloaded metadata")

        for path, data in snapshot.items():
            if restore_paths is not None and path not in restore_paths:
                continue
            if path[0] != "/":
                drive, remainder = path.split(":")[0], path.split(":")[1][1:]
                restore_path = os.path.join(restore_dir, drive, remainder)
            else:
                restore_path = os.path.join(restore_dir, path[1:])
            if data["type"] == "dir":
                os.makedirs(restore_path, exist_ok=True)
                os.utime(restore_path, (data["mtime"], data["mtime"]))
                continue
            os.makedirs(os.path.dirname(restore_path), exist_ok=True)
            start, ostart, end, oend = data["range"]
            with open(restore_path, "wb") as f:
                for i in range(start, end + 1):
                    chunk_path = f"chunks/{chunks[i]}"
                    chunk = self._get_chunk(chunk_path, master)
                    s = ostart if i == start else 0
                    e = oend if i == end else len(chunk)
                    f.write(chunk[s:e])
                    write_size += e - s
            os.utime(restore_path, (data["mtime"], data["mtime"]))
            self.callback(
                f"Restoring: {pretty_bytes(write_size)} / {self._time_str_since_start()}"
            )

        self.logger.info(
            f"Restored {pretty_bytes(write_size)} ({write_size:,} bytes)")
        self.logger.info(f"Restore complete in {self._time_str_since_start()}")

    def get_snapshot_ids(self):
        self.logger.debug("Repo.get_snapshot_ids()")
        snapshot_paths = self.backend.ls("snapshots")
        snapshot_ids = []
        for snapshot_path in snapshot_paths:
            snapshot_id = os.path.basename(snapshot_path)
            snapshot_ids.append(snapshot_id)
        return snapshot_ids

    def prune(self, password):
        if self.backup_start_time is None:
            self.backup_start_time = time.time()
        self.logger.info("Prune started")
        if self.cancel:
            self.logger.info("Stopping")
            return None
        self.callback("Fetching metadata")
        self.snapshot_ids = self.get_snapshot_ids()
        blob_hashes = {
            os.path.basename(path)
            for path in self.backend.ls("chunks")
        }
        self.logger.info(f"Found {len(blob_hashes):,} blobs")
        self.logger.info("Downloaded metadata")
        ref_count = {}
        for blob_hash in blob_hashes:
            ref_count[blob_hash] = 0
        master = self._get_master_key(password)
        for snapshot_id in self.snapshot_ids:
            if self.cancel:
                self.logger.info("Stopping")
                return None
            self.callback(f"Checking: {snapshot_id}")
            self.logger.debug(f"Pruning {snapshot_id}")
            snapshot_obj = decrypt_decompress_obj(
                self.backend.read(f"snapshots/{snapshot_id}"), master)
            try:
                self._ref_count_snapshot_nodes(ref_count, snapshot_obj)
            except KeyError:
                self.logger.error(f"Corrupted snapshot {snapshot_id}")
                raise CorruptSnapshot(snapshot_id)
        deleted = self._prune_using_ref_count(ref_count)
        self.logger.info(f"Pruned {deleted:,} blobs")
        self.logger.info(f"Backup complete in {self._time_str_since_start()}")
        return deleted

    def keep(self, retention):
        if self.cancel:
            return None
        self.logger.debug(f"Repo.keep({retention} days)")
        current_datetime = datetime.datetime.now()
        self.snapshot_ids = self.get_snapshot_ids()
        pool = BoundedThreadPoolExecutor(self.max_thread_queue_size,
                                         self.thread_count)
        for snapshot_id in self.snapshot_ids:
            snapshot_datetime = get_datetime_obj(snapshot_id)
            days_since = (current_datetime - snapshot_datetime).days
            if days_since > retention:
                pool.submit(self._delete, snapshot_id)
        pool.shutdown()

    def _ref_count_snapshot_nodes(self, ref_count, snapshot_obj):
        self.logger.debug("Repo._ref_count_snapshot_nodes()")
        for node in snapshot_obj["snapshot"].values():
            if node["type"] == "file":
                start, ostart, end, oend = node["range"]
                for i in range(start, end + 1):
                    blob_hash = snapshot_obj["chunks"][i]
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
                blob_path = f"chunks/{blob_hash}"
                pool.submit(self._rm_blob, blob_path, deleted)
        pool.shutdown()
        return deleted

    def _delete(self, snapshot_id):
        self.callback(f"Removing: {snapshot_id}")
        self.logger.debug(f"Repo.delete({snapshot_id})")
        snapshot_path = f"snapshots/{snapshot_id}"
        self.backend.rm(snapshot_path)

    def _time_str_since_start(self):
        backup_duration = time.time() - self.backup_start_time
        time_str = str(datetime.timedelta(seconds=int(backup_duration)))
        return time_str

    @lru_cache(maxsize=32)
    def _get_chunk(self, chunk_path, master):
        return decrypt_decompress(self.backend.read(chunk_path), master)

    def _backup_chunk(self, chunk_path, chunk, master):
        self.logger.debug(
            f"Repo._backup_chunk(blob={len(chunk)} bytes, path={chunk_path})")
        if self.cancel:
            return None
        if self.backend.exists(chunk_path):
            return None
        echunk = compress_encrypt(chunk, master, self.compression_level)
        self.write_size_lock.acquire()
        self.write_size += len(echunk)
        self.write_size_lock.release()
        self.backend.write(chunk_path, echunk)

    def _add_dir_to_snapshot(self, snapshot, path):
        self.logger.debug(f"Repo._add_dir_to_snapshot({path})")
        snapshot[path] = {"type": "dir", "mtime": os.path.getmtime(path)}

    def _add_file_to_snapshot(self, snapshot, path, chunk_range):
        self.logger.debug(f"Repo._add_file_to_snapshot({path})")
        snapshot[path] = {
            "type": "file",
            "mtime": os.path.getmtime(path),
            "range": chunk_range
        }

    def _get_master_key(self, password):
        self.logger.debug("Repo._get_master_key()")
        salt = self.backend.read("keys/key-salt")
        return decrypt(self.backend.read("keys/master-key"),
                       generate_key(salt, password))

    def _get_prev_snapshot(self, master):
        snapshots_ids = sorted(self.get_snapshot_ids(), reverse=True)
        if len(snapshots_ids) is 0:
            return {}, []
        snapshot_obj = decrypt_decompress_obj(
            self.backend.read(f"snapshots/{snapshots_ids[0]}"), master)
        return snapshot_obj["snapshot"], snapshot_obj["chunks"]

    def _gen_paths_and_populate(self, include_paths, prev_snapshot, snapshot,
                                exclude_rules):
        for path in self._get_prefix_paths(include_paths) + include_paths:
            try:
                self._add_dir_to_snapshot(snapshot, path)
            except PermissionError:
                self.logger.error(f"Skipped path {path}")
        for path in self._gen_paths(include_paths):
            try:
                if fn_matches(path, exclude_rules):
                    continue
                elif os.path.isdir(path):
                    self._add_dir_to_snapshot(snapshot, path)
                elif os.path.isfile(path):
                    self.processed_size += os.path.getsize(path)
                    if self.cancel:
                        self.callback("Stopping backup")
                        return None
                    else:
                        self.callback(
                            f"{pretty_bytes(self.write_size)} / {pretty_bytes(self.processed_size)}"
                        )
                    if path in prev_snapshot and prev_snapshot[path][
                            "mtime"] == os.path.getmtime(path):
                        snapshot[path] = prev_snapshot[path]
                        continue
                    yield path
                else:
                    self.logger.error(f"Skipped path {path}")
            except PermissionError:
                self.logger.error(f"Skipped path {path}")

    def _gen_paths(self, include_paths):
        for i, include_path in enumerate(include_paths):
            self.logger.info(
                f"Processing {i} / {len(include_paths)} include paths")
            self.logger.info(include_path)
            for root, dirs, files in os.walk(include_path):
                for d in dirs:
                    path = Path(os.path.join(root, d)).as_posix()
                    yield path
                for f in files:
                    path = Path(os.path.join(root, f)).as_posix()
                    yield path

    def _get_prefix_paths_single(self, selected_path):
        self.logger.debug(f"Repo._get_prefix_paths_single({selected_path})")
        prefix_paths = []
        current_dirname = os.path.dirname(selected_path)
        prev_dirname = None
        while True:
            prefix_paths.append(current_dirname)
            current_dirname = os.path.dirname(current_dirname)
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
