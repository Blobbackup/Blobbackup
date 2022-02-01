# Backup Strategy

BlobBackup offers enough flexibility in terms of storage providers,
include/exclude rules and scheduling to be able to craft many 
different backup strategies. You should taylor your backup strategy
to your personal needs and data. But in case you don't know where 
to start, this is how I personally use BlobBackup on my computers.

## 3-2-1 Backup Rule

If you haven’t heard of the 3-2-1 backup strategy before, don’t worry. 
It’s simple. It just means that at any point in time, you have 3 copies 
of the data you want protected, 2 of which will be physically located 
in your house and 1 which will be located outside your house.

For example, if you’re trying to protect your tax documents from 
last year, the 3-2-1 strategy says that you should have 1 copy on your 
computer (the original), 1 on an external hard drive or NAS device, 
and 1 on storage located physically outside your house (a cloud provider, 
a friend’s computer, a server, etc).

This way, in the event that your computer is stolen, your hard drive goes 
“tits up” or (god forbid), your house burns down in a fire, 
your tax documents are still recoverable!

## Storage and Overview

I try to follow the 3-2-1 backup rule for all my computer backups.
I have a local NAS device in my home that receives one copy of my 
data and a Backblaze B2 bucket that receives another. 

I have 3 computers. So on my NAS, I have a folder named 
`backups` that looks like this:

```
/backups
    /macbook
    /dell-xps
    /lenovo
```

And a Backblaze bucket with the same directory layout. Of course, 
there is no such thing as a directory without files in cloud object
storage but you get the idea. We'll let BlobBackup create this 
directory structure for us by specifying the appropriate `prefix`
in the backup configuration.

## What Files to Include/Exclude

I usually backup everything on my home folder and then exclude a 
handful of things that I know I won't ever need to restore. 
Specifically, on my Mac, my include/exclude rules look like this.

Include:
```
/Users/bimbashrestha
```

Exclude:
```
/Users/bimbashrestha/Library*
```

Pretty simple. BlobBackup will report files that it skips (because
of permission issues or other errors). When I come across one of 
these errors, I have a look at the file. If it's some obscure 
cache or system file that won't need to be backed up, I just 
manually add that to my exclude rules. If it's something I believe 
should be backed up but isn't, it might be a bug. 

For most people, I recommend they start by trying to backup their 
entire home folder. If BlobBackup doesn't complain about anything,
you're done! If BlobBackup throws an errors or skips a bunch of files,
manually add those skipped files to your exclusions (if they
are unimportant).

## Backup Schedule

On each computer, I create one backup every hour to my NAS and one 
backup every 2 hours to my Backblaze B2 bucket. I've only had to 
restore files a few times and this seems to work well enough for me. 
Unless you have several TBs of data, BlobBackup should be able to 
complete incremental backups (not initial backups) to any storage 
within 30-40 minutes. Generally, it takes much less time. 

## Backup Retention

On my local NAS backups, I keep a retention of 30 days and on my 
Backblaze B2 bucket, I don't keep a retention and just let 
snapshots accumulate. That might sound space wasteful but BlobBackup's 
compression and de-duplication is good enough that in most cases,
you probably won't notice the difference between that and having 
a 30 day retention.


