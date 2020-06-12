---
layout: post
title: minishift setup for windows 10
subtitle: How to using openshift in local
tags: [technology]
comments: true
---


## what is minishift?

Basically, minishift is a tool that allows you to install and run OpenShift Origin on a local virtual machine.

## how to setup minishift

### download minishift
Download Minishift from [https://github.com/minishift/minishift/releases](https://github.com/minishift/minishift/releases)

Install Virtual Box

Add Minishift folder to PATH, 
-for example: C:\Users\[USER]\minishift-1.34.1 

Add OC foldet to PATH, 
-for example: C:\Users\[USER]\.minishift\cache\oc\v3.11.0\windows 

Make sure Java JDK bin folder is on the path as well, 
-for example: C:\Program Files\Java\jdk1.8.0_221\bin 

Define following docker related environment variables to Windows:
~~~
DOCKER_CERT_PATH=C:\Users\[USER]\.minishift\certs 
DOCKER_HOST=tcp://192.168.99.100:2376 
DOCKER_TLS_VERIFY=1
~~~

### configure and install minishift
Configure Minishift in terminal. 
~~~
minishift config set cpus 4 
minishift config set disk-size 80g 
minishift config set memory 10g 
minishift config set routing-suffix minishift.test 
minishift config set vm-driver virtualbox 
minishift config view
~~~
Setup OpenShift docker registry access 
~~~
minishift addons apply registry-route
~~~
Start Minishift 
~~~
minishift start
~~~
Grant cluster admin rights to developer user: 
~~~
oc login -u system:admin 
oc adm policy add-cluster-role-to-user cluster-admin developer 
oc login -u developer
~~~

Test when installed
~~~
Minishift console 
~~~

from the host machine browser: https://192.168.99.100:8443/console/

Make a shared hotfolder from host machine to Minishift by creating an empty folder to the host machine: 
~~~
minishift hostfolder add --type sshfs --source C:\path\to\the\host\folder --target /mnt/sda1/share share
~~~
Mount the host folder:
~~~
minishift hostfolder mount share
~~~
