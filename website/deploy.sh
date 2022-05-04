#!/bin/bash 

cp server/.env /tmp/.env
cp server/database/database.sqlite /tmp/database.sqlite
git checkout gh-pages
rm -rf **
git checkout master -- website
cp -r website/build_production/** .
rm -rf website
echo "blobbackup.com" > CNAME
git add .
git commit -m "Build for production"
git pull --commit
git push origin gh-pages -f
git reset --hard HEAD
git checkout master
cp /tmp/database.sqlite server/database/database.sqlite
cp /tmp/.env server/.env