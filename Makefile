build_linux:
	cd src && python chunker_setup.py build_ext --inplace
	cd src && pyinstaller application.py \
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
	cd src/dist && zip -r ../../BlobBackup_linux.zip BlobBackup
	cd src && rm -rf BlobBackup.spec dist build chunker.cpython* chunker.c

build_osx:
	cd src && python chunker_setup.py build_ext --inplace
	cd src && pyinstaller application.py \
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
	cp deploy/Info.plist src/dist/BlobBackup.app/Contents/Info.plist
	cd src/dist && zip -r ../../BlobBackup_osx.zip BlobBackup.app
	cd src && rm -rf BlobBackup.spec dist build chunker.cpython* chunker.c

