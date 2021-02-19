from blobbackup.cloud_backend import CloudBackend

from b2sdk.v1 import *
from b2sdk.v1.exception import FileNotPresent, B2ConnectionError, ServiceError
from retry import retry

NUM_TRIES = 10
DELAY = 2


class B2Backend(CloudBackend):
    def __init__(self, key_id, key, bucket, prefix=None):
        CloudBackend.__init__(self, prefix)
        self.bucket = bucket

        self.client = B2Api()
        self.client.authorize_account("production", key_id, key)

    @retry((B2ConnectionError, ServiceError), tries=NUM_TRIES, delay=DELAY)
    def read(self, path):
        dest = DownloadDestBytes()
        self.client.get_bucket_by_name(self.bucket).download_file_by_name(
            self._get_prefixed_path(path), dest)
        return dest.get_bytes_written()

    @retry((B2ConnectionError, ServiceError), tries=NUM_TRIES, delay=DELAY)
    def write(self, path, data):
        self.client.get_bucket_by_name(self.bucket).upload_bytes(
            data, self._get_prefixed_path(path))

    @retry((B2ConnectionError, ServiceError), tries=NUM_TRIES, delay=DELAY)
    def ls(self, path):
        paths = []
        for f, _ in self.client.get_bucket_by_name(
                self.bucket).ls(folder_to_list=self._get_prefixed_path(path)):
            paths.append(self._get_unprefixed_path(f.file_name))
        return paths

    def _versions(self, path):
        versions = list(
            self.client.get_bucket_by_name(self.bucket).list_file_versions(
                self._get_prefixed_path(path)))
        return versions

    @retry((B2ConnectionError, ServiceError), tries=NUM_TRIES, delay=DELAY)
    def exists(self, path):
        return len(self._versions(path)) is not 0

    @retry((B2ConnectionError, ServiceError), tries=NUM_TRIES, delay=DELAY)
    def rm(self, path):
        file_id = [f.id_ for f in self._versions(path)][0]
        self.client.get_bucket_by_name(self.bucket).delete_file_version(
            file_id, self._get_prefixed_path(path))
