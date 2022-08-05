#!/bin/bash

rm -rf restic
git clone -b v0.12.1 https://github.com/restic/restic restic
cd restic
go run build.go
cd -
cp restic/restic src/blobbackup/bin/blobbackup.exe
rm -rf restic