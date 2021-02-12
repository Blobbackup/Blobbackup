from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
from google.auth.exceptions import TransportError
from requests import ConnectionError

from cloud_backend import CloudBackend
from io import BytesIO
from retry import retry

NUM_TRIES = 10
DELAY = 2


class GcpBackend(CloudBackend):
    def __init__(self, cred_file, project, bucket, prefix=None):
        self.bucket = bucket
        self.prefix = prefix

        self.client = storage.Client(
            credentials=service_account.Credentials.from_service_account_file(
                cred_file),
            project=project)

    @retry((TransportError, ConnectionError), tries=NUM_TRIES, delay=DELAY)
    def read(self, path):
        fake_file = BytesIO()
        self.client.bucket(self.bucket).blob(
            self._get_prefixed_path(path)).download_to_file(fake_file)
        fake_file.seek(0)
        return fake_file.read()

    @retry((TransportError, ConnectionError), tries=NUM_TRIES, delay=DELAY)
    def write(self, path, data):
        self.client.bucket(self.bucket).blob(
            self._get_prefixed_path(path)).upload_from_string(data)

    @retry((TransportError, ConnectionError), tries=NUM_TRIES, delay=DELAY)
    def ls(self, path):
        paths = [
            self._get_unprefixed_path(f.name) for f in self.client.list_blobs(
                self.bucket, prefix=self._get_prefixed_path(path))
        ]
        return paths

    @retry((TransportError, ConnectionError), tries=NUM_TRIES, delay=DELAY)
    def exists(self, path):
        return self.client.bucket(self.bucket).blob(
            self._get_prefixed_path(path)).exists()

    @retry((TransportError, ConnectionError), tries=NUM_TRIES, delay=DELAY)
    def rm(self, path):
        self.client.bucket(self.bucket).blob(
            self._get_prefixed_path(path)).delete()
