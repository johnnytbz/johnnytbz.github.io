---
layout: post
title: download single folder or directory from a github
subtitle: how to download a single folder or directory from a github repo
tags: [technology]
comments: true
---


git doesn't support this, but github does via SVN.

### 1.Navigate to the folder you want to download. Let's download /spring-boot/spring-boot-testing from master branch. 

    
![Crepe](/img/docker/image2020-1-14_16-54-11.png) 


### 2.Modify the URL for subversion. Replace tree/master with trunk.

https://github.com/thombergs/code-examples/tree/master/spring-boot/spring-boot-testing ➜

https://github.com/thombergs/code-examples/trunk/spring-boot/spring-boot-testing



### 3.Download the folder. Go to the command line and grab the folder with SVN.

svn checkout https://github.com/thombergs/code-examples/trunk/spring-boot/spring-boot-testing
