#!/bin/bash 

git checkout gh-pages
rm -rf **
git checkout cloud -- website
cp -r website/build_production/** .
rm -rf website
git add .
git commit -m "Build for production"
git pull --commit
git push origin gh-pages