from blobbackup.cloud_backend import CloudBackend
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import (ResourceNotFoundError,
                                   ClientAuthenticationError,
                                   ServiceRequestError, ServiceResponseError)
from retry import retry

NUM_TRIES = 10
DELAY = 2


class AzureBackend(CloudBackend):
    def __init__(self, conn_str, container, prefix):
        CloudBackend.__init__(self, prefix)
        self.container = container

        self.client = BlobServiceClient.from_connection_string(conn_str)

    @retry(
        (ClientAuthenticationError, ServiceRequestError, ServiceResponseError),
        tries=NUM_TRIES,
        delay=DELAY)
    def read(self, path):
        return self.client.get_blob_client(
            container=self.container,
            blob=self._get_prefixed_path(path)).download_blob().readall()

    @retry(
        (ClientAuthenticationError, ServiceRequestError, ServiceResponseError),
        tries=NUM_TRIES,
        delay=DELAY)
    def write(self, path, data):
        self.client.get_blob_client(
            container=self.container,
            blob=self._get_prefixed_path(path)).upload_blob(data,
                                                            overwrite=True)

    @retry(
        (ClientAuthenticationError, ServiceRequestError, ServiceResponseError),
        tries=NUM_TRIES,
        delay=DELAY)
    def ls(self, path):
        paths = [
            self._get_unprefixed_path(f["name"])
            for f in self.client.get_container_client(self.container).
            list_blobs(name_starts_with=self._get_prefixed_path(path))
        ]
        return paths

    @retry(
        (ClientAuthenticationError, ServiceRequestError, ServiceResponseError),
        tries=NUM_TRIES,
        delay=DELAY)
    def exists(self, path):
        try:
            self.client.get_blob_client(
                container=self.container,
                blob=self._get_prefixed_path(path)).get_blob_properties()
            return True
        except ResourceNotFoundError:
            return False

    @retry(
        (ClientAuthenticationError, ServiceRequestError, ServiceResponseError),
        tries=NUM_TRIES,
        delay=DELAY)
    def rm(self, path):
        self.client.get_blob_client(
            container=self.container,
            blob=self._get_prefixed_path(path)).delete_blob()
