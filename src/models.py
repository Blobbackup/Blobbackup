import pickle

from keyring import get_password, delete_password, set_password, set_keyring

import sys

if sys.platform == "win32" or sys.platform == "win64":
    import keyring.backends.Windows
    import win32timezone
elif sys.platform == "linux":
    import keyring.backends.SecretService
elif sys.platform == "darwin":
    import keyring.backends.OS_X

from memory_backend import MemoryBackend
from local_backend import LocalBackend
from aws_backend import AwsBackend
from azure_backend import AzureBackend
from gcp_backend import GcpBackend
from b2_backend import B2Backend
from sftp_backend import SftpBackend

from Crypto.Cipher import AES

import os
import shutil
import requests
import uuid
import getpass
import socket
import platform
import uuid
import base64

NB_DAYS_IN_TRIAL = 14


def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    cipher_text, mac = cipher.encrypt_and_digest(data)
    return cipher.nonce + cipher_text + mac


def decrypt(data, key):
    nonce, cipher_text, mac = data[:16], data[16:-16], data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(cipher_text, mac)


def get_resource_path(path):
    try:
        base_path = sys._MEIPASS
        return os.path.join(base_path, os.path.basename(path))
    except:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, path)


DEFAULT_THREAD_COUNT = 4
DEFAULT_COMPRESSION_LEVEL = 3
DEFAULT_UPLOAD_BLOB_SIZE = 1024
DEFAULT_UPLOAD_SPEED_LIMIT = 0

CHUNK_MIN_EXP = 19
CHUNK_MAX_EXP = 23
HASH_WINDOW_SIZE = 0xfff  # 4095B
HASH_MASK_BITS = 21  # results in ~2MiB chunks statistically

CH_BUZHASH = 'buzhash'
ITEMS_CHUNKER_PARAMS = (CH_BUZHASH, 15, 19, 17, HASH_WINDOW_SIZE)


class Backup(object):
    name = None
    location = None
    password = None
    paths = None
    include_hidden = False
    exclude_rules = None
    follow_symlinks = False

    thread_count = DEFAULT_THREAD_COUNT
    compression_level = DEFAULT_COMPRESSION_LEVEL
    upload_blob_size = DEFAULT_UPLOAD_BLOB_SIZE
    upload_speed_limit = DEFAULT_UPLOAD_SPEED_LIMIT
    enable_variable = False
    min_variable_exp = CHUNK_MIN_EXP
    max_variable_exp = CHUNK_MAX_EXP

    backup_daily_time = None
    backup_days = None
    every_hour = None
    every_min = None
    retention = None

    local_directory = None
    cloud_prefix = None

    s3_url = None

    aws_key_id = None
    aws_key = None
    aws_bucket = None

    gcp_cred_file = None
    gcp_project = None
    gcp_bucket = None

    azure_conn_str = None
    azure_container = None

    b2_key_id = None
    b2_key = None
    b2_bucket = None

    sftp_username = None
    sftp_server = None
    sftp_password = None
    sftp_private_key = None

    def __init__(self):
        pass


class Utils(object):
    @staticmethod
    def get_backend(backup):
        if backup.location == "Memory":
            return MemoryBackend()
        if backup.location == "Local Directory":
            return LocalBackend(backup.local_directory)
        if backup.location == "Amazon AWS":
            return AwsBackend(backup.aws_key_id, backup.aws_key,
                              backup.aws_bucket, backup.cloud_prefix)
        if backup.location == "Microsoft Azure":
            return AzureBackend(backup.azure_conn_str, backup.azure_container,
                                backup.cloud_prefix)
        if backup.location == "Google Cloud":
            return GcpBackend(backup.gcp_cred_file, backup.gcp_project,
                              backup.gcp_bucket, backup.cloud_prefix)
        if backup.location == "Backblaze B2":
            return B2Backend(backup.b2_key_id, backup.b2_key, backup.b2_bucket,
                             backup.cloud_prefix)
        if backup.location == "S3 Storage":
            return AwsBackend(backup.aws_key_id, backup.aws_key,
                              backup.aws_bucket, backup.cloud_prefix,
                              backup.s3_url)
        if backup.location == "SFTP":
            return SftpBackend(backup.sftp_server,
                               backup.sftp_username,
                               backup.cloud_prefix,
                               password=backup.sftp_password,
                               rsa_path=backup.sftp_private_key)


BLOBBACKUP_DIR = os.path.join(os.path.expanduser("~"), ".blobbackup")
MODEL_PATH = os.path.join(BLOBBACKUP_DIR, "config")
SETTINGS_PATH = os.path.join(BLOBBACKUP_DIR, "settings")


class Settings(object):
    @staticmethod
    def get_params():
        if not os.path.exists(BLOBBACKUP_DIR):
            os.makedirs(BLOBBACKUP_DIR)
        try:
            with open(SETTINGS_PATH, "rb") as f:
                params = pickle.load(f)
            return params
        except:
            return {}

    @staticmethod
    def get_param(param):
        try:
            return Settings.get_params()[param]
        except:
            return None

    @staticmethod
    def set_param(param, value):
        params = Settings.get_params()
        params[param] = value
        with open(SETTINGS_PATH, "wb") as f:
            pickle.dump(params, f)


def get_log_file_path(backup_name):
    return os.path.join(BLOBBACKUP_DIR, f"{backup_name}.log")


def set_keyring_multi():
    if sys.platform == "win32" or sys.platform == "win64":
        set_keyring(keyring.backends.Windows.WinVaultKeyring())
    elif sys.platform == "linux":
        set_keyring(keyring.backends.SecretService.Keyring())
    elif sys.platform == "darwin":
        set_keyring(keyring.backends.OS_X.Keyring())


def keyring_works():
    try:
        name = f"blobbackup {uuid.uuid1()}"
        set_keyring_multi()
        set_password(name, "test", "test")
        delete_password(name, "test")
        return True
    except:
        return False


def get_key_in_keyring():
    set_keyring_multi()
    enc_key = get_password("BlobBackup secret", "blobbackup")
    if enc_key is None:
        store_encryption_key_in_keyring()
        enc_key = get_password("BlobBackup secret", "blobbackup")
    key = base64.b64decode(enc_key.encode("ascii"))
    return key


def store_encryption_key_in_keyring():
    key = os.urandom(32)
    enc_key = base64.b64encode(key).decode("ascii")
    set_keyring_multi()
    set_password("BlobBackup secret", "blobbackup", enc_key)


def get_object(data):
    if keyring_works():
        data = decrypt(data, get_key_in_keyring())
    return pickle.loads(data)


def set_object(data):
    data = pickle.dumps(data)
    if keyring_works():
        data = encrypt(data, get_key_in_keyring())
    return data


class Backups(object):
    @staticmethod
    def load_all():
        if not os.path.exists(BLOBBACKUP_DIR):
            if keyring_works():
                store_encryption_key_in_keyring()
            os.makedirs(BLOBBACKUP_DIR)
        try:
            with open(MODEL_PATH, "rb") as f:
                plans = get_object(f.read())
            return plans
        except:
            return {}

    @staticmethod
    def load(name):
        try:
            with open(MODEL_PATH, "rb") as f:
                plans = get_object(f.read())
            plan = plans[name]
            return plan
        except:
            return None

    @staticmethod
    def save(plan):
        plans = Backups.load_all()
        plans[plan.name] = plan
        with open(MODEL_PATH, "wb") as f:
            f.write(set_object(plans))

    @staticmethod
    def delete(name):
        plans = Backups.load_all()
        del plans[name]
        with open(MODEL_PATH, "wb") as f:
            f.write(set_object(plans))