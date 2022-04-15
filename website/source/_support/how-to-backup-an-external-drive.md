---
extends: _layouts.support
title: How to Back up an External Drive
author: Bimba Shrestha
date: 2022-03-16
section: content
---

If you have an external hard drive that you'd like backed up along side your computer data, you 
can do so using Blobbackup. Note that the total amount of data (between both your computer
and your external hard drive) must not exceed 2,000 GB however.

Open up your settings.

![](/assets/images/mac-settings-click.png)

Go to the inclusions tab and click the "Add Folder" button.

![](/assets/images/mac-inclusions-add.png)

Find your external drive (or the folder within your external drive) that you'd like backed up
in the file explorer windows that appears.

![](/assets/images/mac-inclusions-add-external.png)

Click open and save your setting changes. Your external drive should now be backed up the next time a backup runs.
If you'd like to run a backup immediately, you can do so by clicking the "Backup Now"
button (you'll have to stop the backup first if it's already running).

![](/assets/images/mac-start-backup.png)

Once a backup is complete, you can verify that your files have been backed up by clicking
on the "Restore Files" button. You can safely unplug your external hard drive and remove 
the inclusion rule from the settings to go back to just automatically backing up your 
computer.

![](/assets/images/mac-inclusions-remove-external.png)
