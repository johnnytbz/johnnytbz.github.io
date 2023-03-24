---
layout: post
title: some commonly used commands
subtitle: git, docker 
tags: [technology]
comments: false
---
# git command

**git clone**
~~~
git clone git@github.com:username/repos.git
~~~

**git branch**
~~~
git branch --list all branch
git branch NewBranchName  --create branch
git checkout NewBranchName --switch to branch
git branch NewBranchName -d  -- delete branch

~~~

**git push**
~~~
git add . --add all new or modify file to git
git commit -m 'comment this change'
git push
git status --view the current status of the repos
~~~

**git tag**
~~~
git tag V1.2
git push origin V1.2
~~~

**git stash - This command can save the current working state to the git stack**
~~~
git stash -m 'save temporary'
git stash list
git stash pop
git stash show -p stash@{0}
~~~

# docker command

~~~
docker version
docker info

docker images
docker search images_name

docker pull image_name
docker pull image_name:tag

docker run image_name
docker run image_name:tag

docker ps
docker ps -a --include stop 

docker run -it -d --name alias_name images_name:Tag /bin/bash
docker stop container name/container ID
~~~