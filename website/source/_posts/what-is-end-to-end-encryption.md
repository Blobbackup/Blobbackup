---
extends: _layouts.post
title: What is End to End Encryption?
author: Bimba Shrestha
date: 2022-02-02
section: content
description: End to end encryption (E2E) is a phrase that gets thrown around often. Look through the website of any company that handles sensitive data and you’ll see it. But what does end to end encryption actually mean? Let’s look at plain old encryption first...
---

End to end encryption (E2E) is a phrase that gets thrown around often. Look through the website of any company that handles sensitive data and you’ll see it. But what does end to end encryption actually mean? 

Let’s look at plain old encryption first. When you open a website on your browser, you create a connection between your computer and the server that runs that website. By default, this connection is unprotected. Any data sent from your computer is visible to the public.

Thankfully, smart people in the early days of the internet came up with a way to make this better. Secure Socket Layer (SSL) technology allows your computer to create a protected connection between it and the server running the website. 

The cornerstone of SSL is encryption. Encrypting data is like putting something inside a lock box. Without the key, you can’t really do much. SSL puts your data inside a lock box before sending it through the internet. And only the recipient of the lock box has the key.

That’s plain old encryption. It’s what makes it possible to use the internet without having strangers watch everything you do. But notice that SSL only protects your data while it’s on its way. Once the lock box reaches the recipient, It’s easily opened with their key.

This is were E2E comes in. Before placing your data inside SSL’s lock box (whose key the recipient has), you place your data inside your own personal lock box (whose key you keep to yourself). Now your data is inside a lock box inside another.

So even though the recipient is able to open the first lock box, they aren’t able to open your personal one. E2E is stronger than just SSL because it protects your data both in transit, and after delivery—from strangers and the recipient.

SSL is an order of magnitude better than nothing and in many cases, sufficiently secure. But certain cases call for an extra layer of protection. Anytime you cannot or do not want to trust the person or company on the other end of the connection, prefer E2E.

# Encryption in Online Computer Backup

For certain online services, E2E isn’t possible. Any service that requires access to the your original data (online banking for example) cannot use E2E. But for online computer backup, access to your original data is unnecessary. 

Being able to see your data doesn’t (or at least shouldn’t) affect an online backup company’s ability to serve you. Their job is to hold on to your data securely and give it back when you request it. Nothing more and nothing less.

E2E and SSL are not the only positions on data privacy a company can take. There are many others in between. One such position that is relevant to computer backup is E2E with shared key ownership. We’ll call this Shared-E2E. 

In Shared-E2E, you put your data inside a lock box inside another lock box (just like in E2E). But rather than keeping the key to the inner lock box, you share it with the recipient. So while the recipient still has two boxes between them and your data, they also have the ability to open both of them. 

At first, Shared-E2E might sound like it provides no additional privacy over SSL. That isn’t true. For starters, having a second lock box (even if the key is shared) does help. But more importantly, companies who offer Shared-E2E often take special precautions to protect the key to the inner lock box. For example, only trusted admin employees might have access to this key.

# E2E is a Must Have for Backup

Shared-E2E is the most common position taken by online backup companies. For some people, it might be sufficiently private. 

But not for us. We believe companies should only have access to the data they absolutely need for service. [Blobbackup](/) uses E2E. Unlike online banking, whether or not we can see your data has little to do with our ability to provide a robust computer backup service. The data in this case are the files on your computer and the key is your login password. No one, not our employees nor hackers can see your computer data without your password.