---
layout: post
title: docker build mysql master slave
subtitle: build local mysql test env
tags: [technology]
comments: true
---

download docker from : [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

### pull docker image first.
use mysql version 5.7    
~~~
docker pull mysql:5.7
~~~

## download docker

### start the container
where the master and slave containers need to be started separately
mysql Master :
~~~
docker run -p 3339:3306 --name dcpsi-mysql-master -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
~~~
mysql Slave :
~~~
docker run -p 3340:3306 --name dcpsi-mysql-slave -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
~~~
The port of the Master outbound map is 3339, and the port of the Slave outbound map is 3340.


### checking the container if is running
~~~
docker ps
~~~

![Crepe](/img/docker/image2020-1-22_15-1-14.png) 

we can using mysql client connect now.

![Crepe](/img/docker/image2020-6-12_9-50-48.png)

## install Master mysql

### enter the Master container
~~~
docker exec -it dcpsi-mysql-master /bin/bash
~~~

### switch to directory /etc/mysql
~~~
cd /etc/mysql
~~~

### install vim
~~~
apt-get update
apt-get install vim
~~~

### Edit my.cnf
~~~
vi my.cnf
~~~

### append the following configuration in my.cnf:
~~~
[mysqld]
## Be unique in the same LAN
server-id=100 
## Enable binary logging
log-bin=mysql-bin
~~~
### restart service and docker
~~~
service mysql restart
docker start dcpsi-mysql-master
~~~
### create a data synchronization user in the Master database

granting the user slave REPLICATION slave and REPLICATION CLIENT permissions to synchronize data between the Master and slave libraries.

~~~
docker start dcpsi-mysql-master
mysql -uroot -p
CREATE USER 'slave'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%';
~~~

## install Slave mysql

### enter the Slave container
~~~
docker exec -it dcpsi-mysql-slave /bin/bash
~~~

### switch to directory /etc/mysql
~~~
cd /etc/mysql
~~~

### install vim
~~~
apt-get update
apt-get install vim
~~~

### Edit my.cnf
~~~
vi my.cnf
~~~

### append the following configuration in my.cnf:
~~~
[mysqld]
## Be unique in the same LAN
server-id=101 
## Enable binary logging
log-bin=mysql-slave-bin
## config relay_log
relay_log=edu-mysql-relay-bin 
~~~

### restart service and docker
~~~
service mysql restart
docker start
dcpsi-mysql-slave
~~~

## Linking Master and Slave

query mysql in Master
~~~
show master status;
~~~

![Crepe](/img/docker/image2020-1-22_15-5-49.png) 

execute below command line from mysql inslave server.

master_log_file='mysql-bin.000001'
master_log_pos=816
~~~
change master to master_host='172.17.0.2', master_user='slave', master_password='root', master_port=3306, master_log_file='mysql-bin.000001', master_log_pos=816, master_connect_retry=30;
~~~
we can search IP using command:
~~~
docker inspect --format='{{.NetworkSettings.IPAddress}}' dcpsi-mysql-master
~~~

![Crepe](/img/docker/image2020-1-22_15-8-10.png)

execute as follow command on the mysql terminal in Slave;Use to view master-slave synchronization status.
~~~
show Slave status \G;
~~~

![Crepe](/img/docker/image2020-1-22_15-12-38.png)

Start the master-slave replication process using start slave

![Crepe](/img/docker/image2020-1-22_15-11-47.png)

## package installed images to cloud

[https://hub.docker.com](https://hub.docker.com)

if you want upload your docker images to docker hub, sign up an account first.

### package local installed images    

replace your account
~~~
docker commit dcpsi-mysql-master youraccount/mysql-master:mysql-5.7
docker commit dcpsi-mysql-slave youraccount/mysql-slave:mysql-5.7
~~~

### push to cloud
login docker hub
~~~
docker login
~~~

push 
~~~
docker push youraccount/mysql-master:mysql-5.7
docker push youraccount/mysql-slave:mysql-5.7
~~~

![Crepe](/img/docker/image2020-1-22_15-20-53.png) 

