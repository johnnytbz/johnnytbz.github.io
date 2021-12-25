---
layout: post
title: CI/CD brief introduction
subtitle: What is a CI/CD pipeline?
tags: [technology]
comments: true
---


# What is a CI/CD pipeline??

   Continuous integration/continuous delivery

   CI 即持续集成

~~~
持续集成（continuous integration）是在源代码变更后自动检测、拉取、构建和（在大多数情况下）进行单元测试的过程。
目标是快速确保开发人员新提交的变更是好的，并且适合在代码库中进一步使用。
~~~

  CD 可分别指代两个概念： 持续交付 和 持续部署

~~~
持续交付（continuous delivery）通常是指整个流程链（管道），它自动监测源代码变更并通过构建、测试、打包和相关操作运行它们以生成可部署的版本，基本上没有任何人为干预。

持续交付在软件开发过程中的目标是自动化、效率、可靠性、可重复性和质量保障（通过持续测试）。
~~~
~~~
持续部署（continuous deployment）是指能够自动提供持续交付管道中发布版本给最终用户使用的想法。根据用户的安装方式，可能是在云环境中自动部署、app 升级（如手机上的应用程序）、更新网站或只更新可用版本列表。
~~~

Pipeline
~~~
将源代码转换为可发布产品的多个不同的 任务(task)和 作业(job)通常串联成一个软件“管道”，一个自动流程成功完成后会启动管道中的下一个流程。这些管道有许多不同的叫法，例如持续交付管道、部署管道和软件开发管道。
~~~

  ![Crepe](/img/CICD/001.png)

  ![Crepe](/img/CICD/002.png) 

  ![Crepe](/img/CICD/004.jpg)

  ![Crepe](/img/CICD/005.png)

## code style

  组织自定义代码风格：代码缩进，方法名定义，函数不能超过5个等等

  等于是自动review了代码
  

## SonarQube

  SonarQube 是一个开源的代码分析平台, 用来持续分析和评测项目源代码的质量。 
  
  通过SonarQube我们可以检测出项目中重复代码， 潜在bug， 代码规范，安全性漏洞等问题

  SonarQube扫描方法, Jenkins中调用

  SonarQube UI

  ![Crepe](/img/CICD/006.png)

  ![Crepe](/img/CICD/007.png)

  ![Crepe](/img/CICD/008.png)

## OWASP
  
    Open Web Application Security Project

    OWASP是一个开源的、非盈利的全球性安全组织，致力于应用软件的安全研究。
    
    是使应用软件更加安全，使企业和组织能够对应用安全风险做出更清晰的决策

    扫描方法, Jenkins中调用；

## openshift demo

  ![Crepe](/img/CICD/009.png)

~~~
  https://github.com/siamaksade
  https://github.com/siamaksade/openshift-cicd-demo
~~~



