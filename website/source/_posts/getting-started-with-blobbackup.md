---
extends: _layouts.post
title: Getting Started With Blobbackup
author: Bimba Shrestha
date: 2022-02-10
section: content
description: What is Blobbackup? Blobbackup is a tool for backing up your computer. For $9 / month, Blobbackup will backup all user-created data on your Mac or Windows device. Blobbackup creates a mirror clone of the current...
---

# What is Blobbackup?

Blobbackup is a tool for backing up your computer. For $9 / month, Blobbackup will backup all user-created data on your Mac or Windows device. (Please note that there is a 2 TB limit per computer; we’ve found that this limit is well above what most people need).

Blobbackup creates a mirror clone of the current state of your computer every hour (we call this a snapshot). Snapshots are kept for a year. This means that you can recover deleted files or old versions of files going back as far as 1 year.

# How Do I Start Backing Up?

After [signing up](https://app.blobbackup.com/register) for an account with us, you’ll have to download and install Blobbackup on your computer. You can follow our operating system specific guides here: [Mac](/support/how-to-install-blobbackup-on-mac), [Windows](/support/how-to-install-blobbackup-on-windows). (Please note that Blobbackup has not been [code signed](/support/windows-codesign-warnings) yet on Windows so you might see pop up warnings when installing or running the app).

By default, Blobbackup will backup all user-created data on your computer after installation. If you want to change what gets backed up, you can do so from the app Settings. 

# How Do I Restore My Data?

Your data can be restored directly from the Blobbackup app. If you’re trying to restore data to a new or formatted computer, you’ll have to first install Blobbackup. You can follow the restore instructions [here](https://app.blobbackup.com/restore) for details (requires signing in).

Because Blobbackup is [end to end encrypted](/blog/what-is-end-to-end-encryption) with your account password, restores are only possible through the app. We don’t offer restores from the website or via physical hard drive shipment. 

# How Do I Transfer My Service to Another Computer?

To transfer service from computer A to computer B, first, restore files from computer A to computer B (using Blobbackup; or other means if computer A hasn’t been compromised). Then install Blobbackup on computer B and start a fresh backup. Finally, delete computer A from your account dashboard so that we don’t bill you for it. 

(Please note that doing this will not preserve computer A’s backup history; we’re currently working on making backup histories transferable too).  

# How Can I Trust Blobbackup With My Data?

We’ve done a few things to make us more trustable: 1) we’re an [open source](https://github.com/blobbackup/blobbackup) company; all of the code behind our software is available to the public for analysis and audit, 2) we’re [end to end encrypted](/blog/what-is-end-to-end-encryption); we encrypt all computer data with your password so we couldn’t see your data even if we wanted to and 3) we’re simple; we don’t provide unnecessary features or complicated services (we backup your computer securely and that’s it). 

If you have more questions, we’d be happy to [answer them](/support).