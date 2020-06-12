---
layout: post
title: vagrant build mysql master slave
subtitle: using vagrant script build virtualbox for mysql master slave
tags: [technology]
comments: true
---

## how to build a script for vagrant

setup 2 vm , network / system / hostname / access / shell
~~~
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", mount_options: ["dmode=700,fmode=600"]
  config.vm.synced_folder "./config", "/vagrant/config", mount_options: ["dmode=755,fmode=755"]
  
  # run slave first
  config.vm.define "dcpsi-mysqlslave" do |mysqlslave|
    mysqlslave.vm.network "forwarded_port", guest: 3306, host: 33062
    mysqlslave.vm.box = "ubuntu/precise64"
    mysqlslave.vm.hostname = 'dcpsi-mysqlslave'
    mysqlslave.vm.synced_folder "./data/slave", "/var/lib/mysql_vagrant" , id: "mysql",
    owner: 108, group: 113,  # owner: "mysql", group: "mysql",
    mount_options: ["dmode=775,fmode=664"]

    mysqlslave.vm.network :private_network, ip: "192.168.100.12"

    mysqlslave.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "dcpsi-mysqlslave"]
    end

    mysqlslave.vm.provision :shell, path: "bootstrap-slave.sh"
  end


  config.vm.define "dcpsi-mysqlmaster" do |mysqlmaster|
    mysqlmaster.vm.network "forwarded_port", guest: 3306, host: 33061
    mysqlmaster.vm.box = "ubuntu/precise64"
    mysqlmaster.vm.hostname = 'dcpsi-mysqlmaster'
    mysqlmaster.vm.synced_folder "./data/master", "/var/lib/mysql_vagrant" , id: "mysql",
    owner: 108, group: 113,  # owner: "mysql", group: "mysql",
    mount_options: ["dmode=775,fmode=664"]

    mysqlmaster.vm.network :private_network, ip: "192.168.100.11"

    mysqlmaster.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "dcpsi-mysqlmaster"]
    end

    mysqlmaster.vm.provision :shell, path: "bootstrap-master.sh"

  end  
end

~~~

### how to run this script
make sure you install virtualbox and vagrant before you use it.

1.unzip this file

2.using command line into this folder

3.create box
~~~
vagrant up   
~~~

4.login box
~~~
vagrant ssh
~~~

this shell include 2 server,


database forward port : 

master : 33061  slave : 33062

[Vagrant脚本文件下载](/img/docker/vagrant-mysql-master-slave-replication.7z)