---
extends: _layouts.support
title: What is Being Backed Up?
author: Bimba Shrestha
date: 2022-02-25
section: content
---

Blobbackup backs up everything on your computer's primary drive (C drive on Windows and
Macintosh HD on Mac) except files with the following extensions. If you want files with these
extensions backed up, you can update the list from the 
exclusions tab under the [Blobbackup settings](/support/blobbackup-settings).

* *.wab~
* *.vmc
* *.vhd
* *.vo1
* *.vo2
* *.vsv
* *.vud
* *.iso
* *.dmg
* *.sparseimage
* *.sys
* *.cab
* *.exe
* *.msi
* *.dll
* *.dl_
* *.wim
* *.ost
* *.o
* *.qtch
* *.log
* *.ithmb
* *.vmdk
* *.vmem
* *.vmsd
* *.vmsn
* *.vmx
* *.vmxf
* *.menudata
* *.appicon
* *.appinfo
* *.pva
* *.pvs
* *.pvi
* *.pvm
* *.fdd
* *.hds
* *.drk
* *.mem
* *.nvram
* *.hdd

# Mac Specific Exclusions

On Mac, Blobbackup also excludes the following folders.
If you want these folders backed up, you can update the list from the 
exclusions tab under the [Blobbackup settings](/support/blobbackup-settings). 

* /Applications
* /Library
* /Private
* /System
* /bin
* /dev
* /etc
* /net
* /sbin
* /usr
* /home

Note: on Mac, Blobbackup will not backup connected volumes (eg: NAS, Google Drive)
unless the Backup Connected File Systems option is checked under [settings](/support/blobbackup-settings).

# Windows Specific Exclusions

On Windows, Blobbackup also excludes the following folders.
If you want these folders backed up, you can update the list from the 
exclusions tab under the [Blobbackup settings](/support/blobbackup-settings). 

* C:/Windows
* C:/I386
* C:/RECYCLER
* C:/MSOCache
* C:/Program Files
* C:/Program Files (x86)
* C:/Users/All Users/Microsoft
* C:/Users/All Users/Microsoft Help

Note: on Windows, Blobbackup will not backup drives other than the C drive
unless you explicitly include them from the inclusions tab under [settings](/support/blobbackup-settings).