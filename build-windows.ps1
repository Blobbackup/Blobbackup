cd src

python chunker_setup.py build_ext --inplace

pyinstaller .\application.py --noconfirm --onedir --icon .\images\logo.ico --hidden-import=pkg_resources.py2_warn --add-data="images/folder.png;." --add-data="images/logo.ico;." --add-data="images/go.png;." --add-data="images/stop.png;." --add-data="images/edit.png;." --add-data="images/delete.png;." --add-data="images/view.png;."  --windowed --name "BlobBackup"

cp dist/BlobBackup ../BlobBackup
cd ../
