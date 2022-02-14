---
extends: _layouts.support
title: Handling Mounted Volumes on Mac
author: Bimba Shrestha
date: 2022-02-13
section: content
---

By default, Blobbackup backs up everything on your Mac AND everything on any mounted volumes. For example:

* Sync services like Google Drive, Dropbox or Sync.com
* External HDDs and SSDs
* Mounted NAS

To see what volumes are currently mounted, open Finder and press Cmd + Shift + G together. You'll see a dialog box appear. Type "/Volumes" into that dialog box and click Go.

![](/assets/images/mac-finder-volumes.png)

You will then see what volumes you currently have mounted on your Mac. For example, I have 3 volumes: Macintosh HD (the primary volume on every Mac), my Google Drive, and a NAS (home).

![](/assets/images/mac-finder-volumes-show.png)

If you WANT all of these mounted volumes backed up by Blobbackup, you don't have to do anything.

If you DON'T WANT some of these mounted volumes backed up by Blobbackup, you can exclude them by adding an exclusion from the app Settings (see below).

To figure out the path you should be using in your exclusions, right click on your volume from the Finder window (shown above) and click Get Info. For example, I clicked Get Info on my Google Drive Volume and saw this. 

![](/assets/images/mac-google-drive-get-info.png)

Note the circled "Name & Extension". In my case, it's "GoogleDrive". The path I should add to Blobbackup if I want to exclude a volume will be "/Volumes/(Whatever you see under Name & Extension)" (in my case /Volumes/GoogleDrive).

# Exclude a Mounted Volume

Open the Settings window:

![](/assets/images/mac-settings-click.png)

Under the exclusions tab, click add:

![](/assets/images/mac-exclusions-add.png)

Type the exclusion path you want. For example, I'd like to exclude my NAS (/Volumes/home) so I'll type that and click Ok.

![](/assets/images/mac-exclusions-add-dialog.png)

Save your exclusions.

![](/assets/images/mac-exclusions-save.png)

You'll have to restart your backup (if it's currently taking place) for the changes to take effect. To do this, click the Stop Backup button.

![](/assets/images/mac-stop-backup.png)

That same button will turn into the Backup Now button. Click that to restart your backup.

![](/assets/images/mac-start-backup.png)