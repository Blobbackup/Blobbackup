build_linux:
	cd blobbackup && pyinstaller application.py \
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

build_osx:
	cd blobbackup && pyinstaller application.py \
		--noconfirm \
		--icon images/logo.icns \
		--hidden-import=pkg_resources.py2_warn \
		--add-data="images/folder.png:." \
		--add-data="images/logo.icns:." \
		--add-data="images/logo.ico:." \
		--add-data="images/go.png:." \
		--add-data="images/stop.png:." \
		--add-data="images/edit.png:." \
		--add-data="images/delete.png:." \
		--add-data="images/view.png:." \
		--windowed \
		--name "BlobBackup"
	cp deploy/Info.plist blobbackup/dist/BlobBackup.app/Contents/Info.plist
	cp -r blobbackup/dist/BlobBackup.app .
	create-dmg --app-drop-link 0 25 BlobBackup.dmg BlobBackup.app

