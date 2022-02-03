---
extends: _layouts.post
title: What is End to End Encryption?
author: Bimba Shrestha
date: 2022-02-02
section: content
description: End to end encryption (E2E encryption) is a phrase that gets thrown around often. Look through the website of any company that handles sensitive data and you’ll see it. But what does end to end encryption actually mean?
---

End to end encryption (E2E encryption) is a phrase that gets thrown around often. Look through the website of any company that handles sensitive data and you’ll see it. But what does end to end encryption actually mean? 

Let’s look at plain old encryption first. When you open a website on your browser, you create a connection between your computer and the server that runs that website. By default, this connection is unprotected. Any data sent from your computer is visible to the public.

Thankfully, smart people in the early days of the internet came up with a way to make this better. Secure Socket Layer (SSL) technology allows your computer to create a protected connection between it and the server running the website. 

The cornerstone of SSL is encryption. Encrypting data is like putting something in a lock box. Without the key, you can’t really do much. SSL puts your data in a lock box before sending it through the internet. And only the recipient of the box has the key.

That’s plain old encryption. it’s what makes it possible to use the internet without having strangers watch everything you do. But notice that SSL only protects your data while its on its way. Once your lock box reaches the recipient, its easily opened with their key.

This is were E2E encryption comes in. Before placing your data inside SSL’s lock box (whose key the recipient has), you place your data in your own personal lock box (whose key you keep to yourself). Now your data is inside a lock box inside another lock box.

So even though the recipient is able to open the first lock box, they aren’t able to open your personal lock box. E2E encryption is stronger than just SSL because it protects your data both in transit, and after delivery. 

SSL is an order of magnitude better than nothing and in many cases, sufficiently secure. But certain cases simply call for an extra layer of protection. In cases where you cannot or do not wish to trust the person or company on the other end of the connection, prefer E2E encryption.