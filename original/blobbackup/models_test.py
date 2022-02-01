from unittest import TestCase, main

from blobbackup.models import Backup, Utils

from blobbackup.memory_backend import MemoryBackend
from blobbackup.local_backend import LocalBackend
from blobbackup.aws_backend import AwsBackend
from blobbackup.azure_backend import AzureBackend
from blobbackup.gcp_backend import GcpBackend
from blobbackup.b2_backend import B2Backend

from os import environ
import warnings


class ModelsTestCase(TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore",
                                category=ResourceWarning,
                                message="unclosed.*<ssl.SSLSocket.*>")

    def _verify_backend(self, backend, Instance):
        self.assertIsNotNone(backend)
        self.assertIsInstance(backend, Instance)
        self.assertTrue(backend.check_connection())

    def test_get_backend__memory(self):
        backup = Backup()
        backup.location = "Memory"
        self._verify_backend(Utils.get_backend(backup), MemoryBackend)

    def test_get_backend__local(self):
        backup = Backup()
        backup.location = "Local Directory"
        backup.local_directory = "."
        self._verify_backend(Utils.get_backend(backup), LocalBackend)

    def test_get_backend__aws(self):
        backup = Backup()
        backup.location = "Amazon AWS"
        backup.aws_key_id = environ["BLOBBACKUP_AWS_KEY_ID"]
        backup.aws_key = environ["BLOBBACKUP_AWS_KEY"]
        backup.aws_bucket = environ["BLOBBACKUP_AWS_BUCKET"]
        backup.cloud_prefix = "tmp"
        self._verify_backend(Utils.get_backend(backup), AwsBackend)

    def test_get_backend__azure(self):
        backup = Backup()
        backup.location = "Microsoft Azure"
        backup.azure_conn_str = environ["BLOBBACKUP_AZURE_CONN_STR"]
        backup.azure_container = environ["BLOBBACKUP_AZURE_CONTAINER"]
        backup.cloud_prefix = "tmp"
        self._verify_backend(Utils.get_backend(backup), AzureBackend)

    def test_get_backend__gcp(self):
        backup = Backup()
        backup.location = "Google Cloud"
        backup.gcp_cred_file = environ["BLOBBACKUP_GCP_CRED_FILE"]
        backup.gcp_project = environ["BLOBBACKUP_GCP_PROJECT"]
        backup.gcp_bucket = environ["BLOBBACKUP_GCP_BUCKET"]
        backup.cloud_prefix = "tmp"
        self._verify_backend(Utils.get_backend(backup), GcpBackend)

    def test_get_backend__b2(self):
        backup = Backup()
        backup.location = "Backblaze B2"
        backup.b2_key_id = environ["BLOBBACKUP_B2_KEY_ID"]
        backup.b2_key = environ["BLOBBACKUP_B2_KEY"]
        backup.b2_bucket = environ["BLOBBACKUP_B2_BUCKET"]
        backup.cloud_prefix = "tmp"
        self._verify_backend(Utils.get_backend(backup), B2Backend)


if __name__ == "__main__":
    main()
