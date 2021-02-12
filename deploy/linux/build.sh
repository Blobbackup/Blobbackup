#!/bin/bash

# Go into src dir
cd src

# Build the cython chunker module
python chunker_setup.py build_ext --inplace

# Create the binary
pyinstaller application.py \
    --noconfirm \
    --onedir \
    --icon images/logo.ico \
    --hidden-import=pkg_resources.py2_warn \
    --add-data="images/folder.png:." \
    --add-data="images/logo.ico:." \
    --add-data="images/go.png:." \
    --add-data="images/stop.png:." \
    --add-data="images/edit.png:." \
    --add-data="images/delete.png:." \
    --add-data="images/view.png:." \
    --name "BlobBackup"

# Copy built dir
cp -r dist/BlobBackup ../

# Clean artifacts
rm -rf BlobBackup.spec dist build chunker.cpython* chunker.c

# Go back
cd ../
