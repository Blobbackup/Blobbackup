$LATEST_VERSION = Invoke-RestMethod https://app.blobbackup.com/api/client/version
echo "Latest version: $LATEST_VERSION"

$CURRENT_VERSION = type $HOME/.bb/version.txt
echo "Current version: $CURRENT_VERSION"

if ($LATEST_VERSION -gt $CURRENT_VERSION) {
    echo "Current version outdated. Requires update."

    echo "Shutting down Blobbackup processes"
    Stop-Process -Name blobbackup-win
    Stop-Process -Name blobbackup-win32

    echo "Downloading win app"
    Start-BitsTransfer -Source "https://app.blobbackup.com/bin/blobbackup-win-$LATEST_VERSION.zip" -Destination $HOME/.bb/Blobbackup.zip

    echo "Replacing existing app with new one"
    Expand-Archive -Force -Path $HOME/.bb/Blobbackup.zip -DestinationPath $HOME/.bb/blobbackup
    $SIGNED = Get-AuthenticodeSignature $HOME/.bb/blobbackup/blobbackup/blobbackup-win32.exe
    if ($SIGNED.Status -eq "Valid") {
        echo "Codesign verified. Replacing old app"
        Expand-Archive -Force -Path $HOME/.bb/Blobbackup.zip -DestinationPath "C:/Program Files (x86)"
        rm -r -fo $HOME/.bb/blobbackup
        rm -r -fo $HOME/.bb/Blobbackup.zip
    }

    echo "Open new Blobbackup"
    Start-Process "C:/Program Files (x86)/blobbackup/blobbackup-win32.exe" --open-minimized
}