---
extends: _layouts.post
title: Blobbackup 1.0.8 Released
author: Bimba Shrestha
date: 2022-03-15
section: content
description: We released version 1.0.8 of the Blobbackup desktop app (Mac and Windows). This update contains several bug fixes and user experience improvements. We highly recommend everyone upgrade to this. Download the...
---

We released version 1.0.8 of the Blobbackup desktop app (Mac and Windows). This update contains several bug fixes and user experience improvements. We highly recommend everyone upgrade to this.

# Bug Fixes

* Fix backup scheduler bug that prevented automatic backups from running after computer sleeps for more than 8 hours.
* Fix Windows task scheduler elevated permissions bug that prevented Blobbackup from starting automatically on startup.
* Fix bug that caused the UI to glitch for a second when backup is terminated by network loss.
* Fix Windows bug where command prompt appeared for a few seconds when running some operations.

# Other Improvements

* Move advanced options into their own tab under app settings.
* Start Blobbackup "silently" on startup without showing the control panel.
* More verbose logging.

# Upgrade Methods

To upgrade to version 1.0.8, just download and install it on your computer (make sure to "Quit" the current app before installing). Your existing Blobbackup installation will automatically be overridden.

**Mac Upgrade**

Step 0: Quit Blobbackup if it's currently running using the menu bar icon.

<img src="/assets/images/mac-quit.png" class="m-10">

Step 1: Download version 1.0.8 ([Intel Mac](https://app.blobbackup.com/bin/blobbackup-darwin-amd-1.0.8.dmg), [M1 Mac](https://app.blobbackup.com/bin/blobbackup-darwin-arm-1.0.8.dmg)) and open it.

<img src="/assets/images/mac-installer.png" class="md:w-1/2">

Step 2: Drag the Blobbackup app into the Applications folder.

<img src="/assets/images/mac-drag.png" class="md:w-1/2">

Done! Now just open Blobbackup from your Applications folder.

**Windows Upgrade**

Step 0: Quit Blobbackup if it's currently running using the system tray icon.

Step 1: Download version 1.0.8 ([Windows](https://app.blobbackup.com/bin/blobbackup-win-1.0.8.exe)) and open it.

<img src="/assets/images/win-installer1.png" class="my-8"/>

Step 2: Follow the steps on the installer and launch Blobbackup at the end.

Done!