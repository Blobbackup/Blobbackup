from gcp_backend import GcpBackend

import os
import sys

file_name = sys.argv[-1]

backend = GcpBackend("creds/gcp.json", "bloobs-test", "blobbackup", "releases")
with open(file_name, "rb") as f:
    backend.write(os.path.basename(file_name), f.read())

print(f"Uploaded {file_name} to blobbackup")