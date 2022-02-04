#!/bin/bash

cd ../

ssh $1 'rm -rf ~/blobbackup'

scp -r client $1:~/blobbackup

ssh $1 'export PATH=$PATH:/usr/local/bin:/Users/bikushrestha/miniconda3/bin && cd blobbackup && ./src/blobbackup/scripts/buildosx.sh && python3 package/fix_qt_for_codesign.py dist/Blobbackup.app && tar -zcvf dist.tar.gz dist'

scp $1:~/blobbackup/dist.tar.gz client

tar -xvf client/dist.tar.gz -C client

cd client/dist

../package/macos-package-app.sh
