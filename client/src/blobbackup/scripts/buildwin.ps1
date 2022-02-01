src/blobbackup/scripts/generateui.ps1
pip install .
pyinstaller --clean --noconfirm package/blobbackup.spec
rm build -r -fo