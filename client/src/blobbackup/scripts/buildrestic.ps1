rm -r -fo restic
git clone -b v0.12.1 https://github.com/restic/restic restic
cd restic
go run build.go
cd ../
cp restic/restic.exe src/blobbackup/bin/blobbackup.exe
rm -r -fo restic