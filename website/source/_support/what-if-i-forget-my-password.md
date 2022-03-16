---
extends: _layouts.support
title: What if I Forget My Password?
author: Bimba Shrestha
date: 2022-03-13
section: content
---

Blobbackup doesn't let you reset your password if you forget it. This is by design.

Blobbackup's design is inspired by password managers. And just like password managers,
Blobbackup uses the "primary" password you create when registering to encrypt your important 
data (backups in our case, passwords in the case of password managers).

This means the only way someone can access your data is if they know your encryption
password. We don't know your encryption password so we can't access your data or 
"reset" your password if you forget it. 

Note: you can still change your password as long as you know your current one from 
your account's settings.