from google.oauth2 import service_account
from backend import PathNotFound
from cloud_backend import CloudBackend
from fs.googledrivefs import GoogleDriveFS
from fs.walk import Walker
from fs.path import join
from fs.errors import ResourceNotFound
from googleapiclient.errors import ResumableUploadError, HttpError
from google.auth.transport.requests import Request
from retry import retry
from socket import timeout

import time
import pickle


class GDriveBackend(CloudBackend):
    def __init__(self, creds_path, prefix):
        CloudBackend.__init__(self, prefix)
        with open(creds_path, "rb") as f:
            self.cred = pickle.load(f)
        if self.cred.expired and self.cred.refresh_token:
            self.cred.refresh(Request())
            with open(creds_path, "wb") as f:
                pickle.dump(self.cred, f)

    def _get_fs(self):
        return GoogleDriveFS(self.cred)

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def makedirs(self, path):
        self._get_fs().makedirs(self._get_prefixed_path(path), recreate=True)

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def read(self, path):
        try:
            return self._get_fs().readbytes(self._get_prefixed_path(path))
        except ResourceNotFound:
            raise PathNotFound(path)

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def write(self, path, data):
        self._get_fs().writebytes(self._get_prefixed_path(path), data)

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def ls(self, path):
        paths = []
        for root, _, files in Walker().walk(
                self._get_fs(), path=self._get_prefixed_path(path)):
            for f in files:
                p = join(root, f.name)[1:]
                paths.append(self._get_unprefixed_path(p))
        return paths

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def exists(self, path):
        return self._get_fs().exists(self._get_prefixed_path(path))

    @retry((ResourceNotFound, ResumableUploadError, HttpError, timeout),
           tries=10,
           delay=2)
    def rm(self, path):
        self._get_fs().remove(self._get_prefixed_path(path))
