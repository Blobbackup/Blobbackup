from boto3 import client

from backend import PathNotFound
from cloud_backend import CloudBackend
from botocore.exceptions import ReadTimeoutError, ConnectionClosedError
from urllib3.exceptions import ProtocolError
from retry import retry

NUM_TRIES = 10
DELAY = 2


class AwsBackend(CloudBackend):
    def __init__(self, key_id, key, bucket, prefix=None, url=None):
        CloudBackend.__init__(self, prefix)
        self.bucket = bucket
        self.client = client("s3",
                             endpoint_url=url,
                             aws_access_key_id=key_id,
                             aws_secret_access_key=key)

    @retry((ReadTimeoutError, ConnectionClosedError, ProtocolError),
           tries=NUM_TRIES,
           delay=DELAY)
    def read(self, path):
        return self.client.get_object(
            Bucket=self.bucket,
            Key=self._get_prefixed_path(path))["Body"].read()

    @retry((ReadTimeoutError, ConnectionClosedError, ProtocolError),
           tries=NUM_TRIES,
           delay=DELAY)
    def write(self, path, data):
        self.client.put_object(Bucket=self.bucket,
                               Body=data,
                               Key=self._get_prefixed_path(path))

    @retry((ReadTimeoutError, ConnectionClosedError, ProtocolError),
           tries=NUM_TRIES,
           delay=DELAY)
    def ls(self, path):
        prefixed_path = self._get_prefixed_path(path)
        res = self.client.list_objects_v2(Bucket=self.bucket,
                                          Prefix=prefixed_path)
        if "Contents" not in res:
            return []
        keys = [self._get_unprefixed_path(f["Key"]) for f in res["Contents"]]
        while res["IsTruncated"]:
            res = self.client.list_objects_v2(
                Bucket=self.bucket,
                Prefix=prefixed_path,
                ContinuationToken=res["NextContinuationToken"])
            if "Contents" not in res:
                break
            keys.extend(
                [self._get_unprefixed_path(f["Key"]) for f in res["Contents"]])
        return keys

    @retry((ReadTimeoutError, ConnectionClosedError, ProtocolError),
           tries=NUM_TRIES,
           delay=DELAY)
    def exists(self, path):
        try:
            self.client.head_object(Bucket=self.bucket,
                                    Key=self._get_prefixed_path(path))
            return True
        except self.client.exceptions.ClientError:
            return False

    @retry((ReadTimeoutError, ConnectionClosedError, ProtocolError),
           tries=NUM_TRIES,
           delay=DELAY)
    def rm(self, path):
        self.client.delete_object(Bucket=self.bucket,
                                  Key=self._get_prefixed_path(path))
