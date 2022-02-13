---
extends: _layouts.support
title: How to Exclude External Storage on Mac?
author: Bimba Shrestha
date: 2022-02-10
section: content
---

If you have a NAS or external drives connected to your Mac and you DON'T want them backed up, this page shows you how to exclude them.

# Exclude All External Storage

Open the Settings window:

![](/assets/images/mac-settings-click.png)

Under the exclusions tab, click add:

![](/assets/images/mac-exclusions-add.png)

Type the exclusion "/Volumes" and click Ok.

![](/assets/images/mac-exclusions-add-dialog.png)

Save your exclusions.

![](/assets/images/mac-exclusions-save.png)

You'll have to restart your backup (if it's currently taking place) for the changes to take effect. To do this, click the Stop Backup button.

![](/assets/images/mac-stop-backup.png)

That same button will turn into the Backup Now button. Click that to restart your backup.

![](/assets/images/mac-start-backup.png)

# Don't Exclude All Volumes

Excluding "/Volumes" might mean some mounted folders on your computer (ie: Dropbox, Google Drive, Sync.com) get excluded too. The easiest way to make sure those mounted folders don't get excluded is to manually include them. Here is how:

Open the Settings window:

![](/assets/images/mac-settings-click.png)

Under the inclusions tab, click Add Folder:

![](/assets/images/mac-inclusions-add.png)

Find and open the folder that you want to manually include (this will override any higher level exclusions). I've selected a folder on my NAS for example:

![](/assets/images/mac-inclusions-add-dialog.png)

Save your settings:

![](/assets/images/mac-inclusions-save.png)

You'll have to restart your backup (if it's currently taking place) for the changes to take effect. To do this, click the Stop Backup button.

![](/assets/images/mac-stop-backup.png)

That same button will turn into the Backup Now button. Click that to restart your backup.

![](/assets/images/mac-start-backup.png)