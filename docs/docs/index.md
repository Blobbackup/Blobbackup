![Logo](images/logo.png)

# BlobBackup Documentation

Welcome to the BlobBackup Documentation. If you find something
confusing, missing or wrong, please file an issue on our 
[Github](https://github.com/bimbashrestha/blobbackup) page! 

## What is BlobBackup?

Simply put, BlobBackup is a desktop application for Windows, Mac
and Linux computers that copies your data somewhere else in a "smart"
way. So if something bad happens to the original copy, you have a backup
that you can recover from. Sound too simple for a dedicated tool? Don't worry,
there is a quite a bit more under the hood! 

BlobBackup does a number of things to help you get the most out 
of your backups. Here are some of the highlights.

### Extensive Storage Support

Have a computer or NAS in your home with some space? Or maybe 
you have a cloud storage provider like AWS, Google, or Backblaze? 
If you have some extra storage somewhere that you'd like to put to use,
chances are BlobBackup will let you create backups to it! As of right
now, BlobBackup supports the following storage providers: SFTP, Amazon S3,
Local Storage, Network Storage (NAS or Network Computer),
S3 Compatible Storage (Wasabi, MinIO, etc), Google Cloud Storage,
Microsoft Azure Blob, and Backblaze B2.

Note: Support for Google Drive and OneDrive coming soon.

### Automation

BlobBackup automates your backups to run in the background. Configure 
your schedule once, save it, and never think about your backups again
(or at least not until the dreaded day you need a restore). All the 
scheduling happens directly in the app so there is no need to manually
set up cron jobs, launch agents, or Windows tasks.

### Efficient Data Format

BlobBackup doesn't just copy your data from your computer to
your storage. You can do that on your own! Where BlobBackup really 
shines is when you create multiple backups over time. Because of the 
way BlobBackup stores your data (using block level de-duplication,  
advanced compression, incremental snapshots, etc), you can (generally
speaking) store versioned copies of all your data over time FOREVER 
and STILL use less space on your backup storage than your original data
size. 

### End to End Encryption


