# BlobBackup Data Format

The BlobBackup data format receives inspiration from a number of 
wonderful open source projects. Most notably: [Duplicacy](https://github.com/gilbertchen/duplicacy), 
[Restic](https://github.com/restic/restic), [Borg](https://github.com/borgbackup/borg), and 
[Duplicati](https://github.com/duplicati/duplicati). 

## Directory Structure

```
Backup
├── chunks
│   ├── ffec855a0d5062fc1056d13e62c1c77dc5462801e5d40b7485661d47067a351b (1 - 16 MB in size)
│   ├── fff3e0f77130ff74c9d75dd9278ded30ac07c40d9c7a720e575f988f514e58e3 (1 - 16 MB in size)
│   └── fffe2a9e8dfa232e40ada1487264630e6ac19a653be7bc1bcc1e84bb84443231 (1 - 16 MB in size)
│   ├── ...
├── keys
│   ├── key-salt (Salt used for key derivation from user password)
│   ├── master-key (Random bytes encrypted with the derived key)
│   └── sha-key (Key used for HMAC hashing encrypted with master)
└── snapshots
    ├── 2021-02-13-09-26-41 (Format %Y-%m-%d-%H-%M-%S)
    ├── 2021-02-13-09-28-25
    ├── 2021-02-13-10-36-41
```

When the user first creates a backup repository, two keys are 
randomly generated, the `master-key` and the `sha-key`. The `sha-key`
is encrypted using the `master-key` before getting stored. And the 
`master-key` is encrypted using a key derived from the user's 
password before getting stored. The key derivation algorithm 
used is `scrypt`.

## Snapshot Format

```
{
    "data_format_version": 1,
    "snapshot": {
        "/home/bimbashrestha/Downloads": {
            "type": "dir",
            "mtime": 1234567.12
        },
        "/home/bimbashrestha/notes.txt": {
            "type": "file",
            "mtime": 1234566.12,
            "range": [0, 4321, 1, 123456]
        },
        "/home/bimbashrestha/Downloads/download.sh": {
            "type": "file",
            "mtime": 1234562.12,
            "range": [1, 123456, 3, 1234]
        }
    },
    "chunks": [
        "ffec855a0d5062fc1056d13e62c1c77dc5462801e5d40b7485661d47067a351b",
        "fff3e0f77130ff74c9d75dd9278ded30ac07c40d9c7a720e575f988f514e58e3",
        "fffe2a9e8dfa232e40ada1487264630e6ac19a653be7bc1bcc1e84bb84443231"
    ]
}
```

Snapshot files are encrypted and compressed json files in the format
above.

## Chunking

BlobBackup uses variable length chunking using the buzhash hash algorithm. 
The chunker code is adopted from the [Borg](https://github.com/borgbackup/borg)
open source project. 

BlobBackup treats all files as one long stream of bytes. That is, if 
the end of a file has been reached but the chunker has not reached 
a terminating point, then BlobBackup will continue onto the next file 
as though it were concatenated. This technique is adopted from the 
[Duplicacy](https://github.com/gilbertchen/duplicacy) open source 
project.

All chunks are between 1 MB and 16 MB in size to allow for decent 
upload speeds.

## Encryption

All BlobBackup files (other than `keys/key-salt`) are encrypted using
256 bit AES in GCM mode. The format of encrypted blobs is the following: 

```
IV || CIPHER_TEXT || MAC
```

The `IV` and `MAC` are both 16 bytes in length.

## Compression

BlobBackup uses [Zstandard](https://github.com/facebook/zstd) to 
compress chunks before they are encrypted.

