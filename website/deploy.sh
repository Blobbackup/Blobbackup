#!/bin/bash 

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
git checkout master