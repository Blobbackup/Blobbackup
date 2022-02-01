#!/usr/bin/env bash
# Inspired by https://github.com/metabrainz/picard/blob/master/scripts/package/macos-notarize-app.sh
# Take from https://github.com/borgbase/vorta/blob/master/package/macos-package-app.sh

set -eux

APP_BUNDLE_ID="com.blobbackup.client.macos"
APP_BUNDLE="Blobbackup"
# CERTIFICATE_NAME=""
# APPLE_ID_USER=""
# APPLE_ID_PASSWORD=""

find $APP_BUNDLE.app/Contents/Resources/ \
    -type f \( -name \*.so -or -name \*.dylib -or -name blobbackup.exe -or -name blobbackup -or -name Python \) \
    -exec codesign --verbose --force --timestamp --deep --sign "${CERTIFICATE_NAME}" \
    --entitlements ../package/entitlements.plist  --options runtime {} \;

codesign --verify --force --verbose --deep \
        --options runtime --timestamp \
        --entitlements ../package/entitlements.plist \
        --sign "$CERTIFICATE_NAME" $APP_BUNDLE.app

# Create DMG
rm -rf $APP_BUNDLE.dmg
create-dmg \
  --volname "Blobbackup Installer" \
  --window-size 410 300 \
  --icon-size 100 \
  --icon "Blobbackup.app" 70 150 \
  --hide-extension "Blobbackup.app" \
  --app-drop-link 240 150 \
  "Blobbackup.dmg" \
  "Blobbackup.app"

# Notarize DMG
RESULT=$(xcrun altool --notarize-app --type osx \
    --primary-bundle-id $APP_BUNDLE_ID \
    --username $APPLE_ID_USER --password $APPLE_ID_PASSWORD \
    --file "$APP_BUNDLE.dmg" --output-format xml)

REQUEST_UUID=$(echo "$RESULT" | xpath5.18 "//key[normalize-space(text()) = 'RequestUUID']/following-sibling::string[1]/text()" 2> /dev/null)

# Poll for notarization status
echo "Submitted notarization request $REQUEST_UUID, waiting for response..."
sleep 60
while true
do
  RESULT=$(xcrun altool --notarization-info "$REQUEST_UUID" \
    --username "$APPLE_ID_USER" \
    --password "$APPLE_ID_PASSWORD" \
    --output-format xml)
  STATUS=$(echo "$RESULT" | xpath5.18 "//key[normalize-space(text()) = 'Status']/following-sibling::string[1]/text()" 2> /dev/null)

  if [ "$STATUS" = "success" ]; then
    echo "Notarization of $APP_BUNDLE succeeded!"
    break
  elif [ "$STATUS" = "in progress" ]; then
    echo "Notarization in progress..."
    sleep 20
  else
    echo "Notarization of $APP_BUNDLE failed:"
    echo "$RESULT"
    exit 1
  fi
done

# Staple the notary ticket
xcrun stapler staple $APP_BUNDLE.dmg
xcrun stapler staple $APP_BUNDLE.app
xcrun stapler validate $APP_BUNDLE.dmg
