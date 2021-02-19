from blobbackup.cloud_backend import CloudBackend
from pysftp import Connection, ConnectionException, CnOpts
from paramiko.ssh_exception import SSHException
from retry import retry

import os

NUM_TRIES = 10
DELAY = 2


class SftpBackend(CloudBackend):
    def __init__(self, server, username, prefix, password=None, rsa_path=None):
        CloudBackend.__init__(self, prefix)
        self.server = server
        self.username = username
        self.password = password
        self.prefix = prefix
        self.rsa_path = rsa_path
        self.cnopts = CnOpts()
        self.cnopts.hostkeys = None

    def _get_connection(self):
        return Connection(self.server,
                          username=self.username,
                          private_key=self.rsa_path,
                          password=self.password,
                          cnopts=self.cnopts)

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def makedirs(self, path):
        with self._get_connection() as sftp:
            if not sftp.exists(self._get_prefixed_path(path)):
                sftp.makedirs(self._get_prefixed_path(path))

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def read(self, path):
        with self._get_connection() as sftp:
            with sftp.open(self._get_prefixed_path(path), "rb") as f:
                return f.read()

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def write(self, path, data):
        with self._get_connection() as sftp:
            dirname = os.path.dirname(path)
            if not sftp.exists(self._get_prefixed_path(dirname)):
                sftp.makedirs(self._get_prefixed_path(dirname))
            with sftp.open(self._get_prefixed_path(path), "wb") as f:
                f.write(data)

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def ls(self, path):
        paths = []
        with self._get_connection() as sftp:
            sftp.walktree(
                self._get_prefixed_path(path),
                lambda path: paths.append(self._get_unprefixed_path(path)),
                lambda _: None, lambda _: None, True)
        return paths

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def exists(self, path):
        with self._get_connection() as sftp:
            return sftp.exists(self._get_prefixed_path(path))

    @retry((SSHException, ConnectionException), tries=NUM_TRIES, delay=DELAY)
    def rm(self, path):
        with self._get_connection() as sftp:
            sftp.remove(self._get_prefixed_path(path))
