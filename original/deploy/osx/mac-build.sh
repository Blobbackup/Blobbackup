source build.sh
cp creds/Info.plist dist/BlobBackup.app/Contents/Info.plist
codesign --entitlements entitlements.plist --options runtime --force --deep --sign "Developer ID Application: Bimba Shrestha (9BLKG2356L)" dist/BlobBackup.app

# 0. use dmg canvas to create with "code sign without notirization"

# 1. xcrun altool -t osx -f dist/BlobBackup_osx_v0.1.1_setup.dmg --primary-bundle-id BlobBackup --notarize-app --username support@blobbackup.com
# provide password from apple

# 2. xcrun altool --notarization-info "c004e79a-847e-489a-bea8-0f5dedf122f8" -u support@blobbackup.com
# provide password from apple

# 3. xcrun stapler staple -v dist/BlobBackup_osx_v0.1.1_setup.dmg

# following instructions from https://forum.xojo.com/t/how-to-codesign-and-notarise-your-app-for-macos-10-14-and-higher/45879