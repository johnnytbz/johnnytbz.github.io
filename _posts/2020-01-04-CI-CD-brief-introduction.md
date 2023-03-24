---
layout: post
title: CI/CD brief introduction
subtitle: What is a CI/CD pipeline?
tags: [technology]
comments: true
---


# What is a CI/CD pipeline??

   Continuous integration/continuous delivery

   CI continuous integration

~~~
Continuous integration is the process of automatically detecting, pulling, 
building and (in most cases) unit testing after source code changes.

The goal is to quickly ensure that a developer's newly committed changes are good 
and suitable for further use in the codebase.
~~~

  CD can refer to two concepts respectively: continuous delivery and continuous deployment.

~~~
Continuous delivery generally refers to the entire process chain (pipeline) that 
automatically monitors source code changes and runs them through building, testing, 
packaging and related operations to produce a deployable version, basically without any human intervention.

The goals of continuous delivery in the software development process are automation, 
efficiency, reliability, repeatability, and quality assurance (through continuous testing).
~~~

~~~
Continuous deployment refers to the idea of being able to automatically deliver releases from a continuous delivery pipeline to end users. Depending on how the user installed it, it could be an automatic deployment in a cloud environment, an app upgrade (like an app on a phone), an update to a website, or just an update to the list of available versions.
~~~

Pipeline
~~~
  The many different tasks and jobs that transform source code into a releasable product are often chained together into a software pipeline with the successful completion of one automated process starting the next process in the pipeline. These pipelines go by many different names, such as continuous delivery pipelines, deployment pipelines, and software development pipelines.
~~~

  ![Crepe](/img/CICD/001.png)

  ![Crepe](/img/CICD/002.png) 

  ![Crepe](/img/CICD/004.jpg)

  ![Crepe](/img/CICD/005.png)

## code style

  Organize custom code style: code indentation, method name definition, no more than 5 functions, etc.

  It is equivalent to automatically reviewing the code
  

## SonarQube

  SonarQube is an open source code analysis platform used to continuously analyze and evaluate the quality of project source code.
  
  Through SonarQube, we can detect duplicate code, potential bugs, code specifications, security vulnerabilities and other issues in the project

  SonarQube scanning method, called in Jenkins

  SonarQube UI

  ![Crepe](/img/CICD/006.png)

  ![Crepe](/img/CICD/007.png)

  ![Crepe](/img/CICD/008.png)

## OWASP
  
    Open Web Application Security Project

    OWASP is an open source, non-profit global security organization dedicated to application software security research.
    
    It is to make application software more secure and enable enterprises and organizations to make clearer decisions about application security risks

    Scan method, called in Jenkins;

## openshift demo

  ![Crepe](/img/CICD/009.png)

~~~
  https://github.com/siamaksade
  https://github.com/siamaksade/openshift-cicd-demo
~~~



