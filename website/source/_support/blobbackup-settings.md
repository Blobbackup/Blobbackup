---
extends: _layouts.support
title: Blobbackup Settings
author: Bimba Shrestha
date: 2022-02-25
section: content
---

You can open the settings window from the Blobbackup control panel
by clicking the Settings button.

![](/assets/images/mac-settings-click.png)

# General Settings

Under the general settings tab, you can change the:

* **Computer Name**: the identifier for your computer. By default, we pick your computer's 
hostname but you can change this to anything you want. Changing this does not impact
backups at all.
* **Backup Schedule**: when to run your backups. Automatic (recommended) means Blobbackup will create a 
backup every hour. Manual means Blobbackup will only backup when you click the 
Backup Now button.
* **Max Upload KiB/s**: the maximum upload bandwidth allowed. 0 (recommended) means there is no limit.
This can be useful if you have bandwidth limits from your ISP or if you want Blobbackup to use 
less bandwidth while running.
* **Backup Connected File Systems (only on Mac)**: by default, Blobbackup does not backup connected 
volumes (eg: NAS, Google Drive, Dropbox). Enable this to backup those too.

![](/assets/images/mac-general-settings.png)

# Inclusions Settings

Under the inclusions settings, you can select what folders you want backed up. By
default, Blobbackup backs up everything under "/" on Mac and everything under the 
"C" drive on Windows.

Click the Add Folder button to select and add a folder on your computer for backup.
Click the Remove button while selecting an existing folder to remove it.

![](/assets/images/mac-inclusions-settings.png)

# Exclusions Settings

Under the exclusions settings, you can edit what gets excluded from your backups.
By default, Blobbackup excludes the [following](/support/what-is-backed-up). 

Click the Add button to add a new exclusion rule. Click the Remove button while 
selecting an existing rule to remove it.

* To exclude a folder, add the full path of the folder as an exclusion rule. For example,
if I wanted to exclude my Downloads folder on Mac, I'd add the exclusion rule 
"/Users/bimba/Downloads". And if I wanted to exclude the Downloads folder on my PC,
I'd add the exclusion rule "C:/Users/bimba/Downloads". Contact [support](/support)
if you have any specific questions.
* To exclude all files with a specific extension, add the name of the extension with 
an "\*" at the beginning. For example, if I wanted to exclude all files with the ".mov"
extension, I'd add the exclusion rule "\*.png".

![](/assets/images/mac-exclusions-settings.png)