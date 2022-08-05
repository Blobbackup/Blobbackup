src/blobbackup/scripts/buildrestic.ps1
src/blobbackup/scripts/generateui.ps1
pip install .
pyinstaller --clean --noconfirm package/blobbackup.spec
rm build -r -fo