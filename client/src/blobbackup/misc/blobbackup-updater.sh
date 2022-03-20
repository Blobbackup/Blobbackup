#!/bin/bash

LATEST_VERSION=$(curl https://app.blobbackup.com/api/client/version)
echo "Latest version:" $LATEST_VERSION

CURRENT_VERSION=$(cat ~/.bb/version.txt)
echo "Current version:" $CURRENT_VERSION

if [[ $LATEST_VERSION > $CURRENT_VERSION ]]; then
    echo "Current version outdated. Requires update."
    
    echo "Shutting down Blobbackup processes"
    for PID in $(ps -ax | grep /Applications/Blobbackup.app/Contents/MacOS/blobbackup-darwin | awk '{print $1}'); do
        kill -9 $PID
        echo "Killed" $PID
    done
    for PID in $(ps -ax | grep /Applications/Blobbackup.app/Contents/MacOS/bin/blobbackup-darwin-amd | awk '{print $1}'); do
        kill -9 $PID
        echo "Killed" $PID
    done

    if [[ $(uname -m) == 'arm64' ]]; then
        echo "Downloading arm app"
        curl https://app.blobbackup.com/bin/blobbackup-darwin-arm-{$LATEST_VERSION}.dmg -o /tmp/Blobbackup.dmg
    else
        echo "Downloading amd app"
        curl https://app.blobbackup.com/bin/blobbackup-darwin-amd-{$LATEST_VERSION}.dmg -o /tmp/Blobbackup.dmg
    fi

    echo "Replacing existing app with downloaded one"
    hdiutil attach -nobrowse -mountpoint /Volumes/Blobbackup /tmp/Blobbackup.dmg
    if codesign --verify /Volumes/Blobbackup/Blobbackup.app; then
        echo "Codesign verified. Replacing old app"
        rm -rf /Applications/Blobbackup.app
        cp -R /Volumes/Blobbackup/Blobbackup.app /Applications/Blobbackup.app
    fi
    hdiutil detach /Volumes/Blobbackup
fi