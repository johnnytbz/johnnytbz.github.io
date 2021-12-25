---
layout: post
title: Microservice brief introduction
subtitle: How to understand micro service
tags: [technology]
comments: true
---


# What is Microservice?


## Monolithic applications

![Crepe](/img/microservice/p004.png)

### model 1

要理解什么是微服务，那么可以先理解什么是单体应用，

在没有提出微服务的概念的“远古”年代，一个软件应用，往往会将应用所有功能都开发和打包在一起，

那时候的一个B/S应用架构往往是这样的

![Crepe](/img/microservice/p001.png)

### model 2

当用户访问量变大导致一台服务器无法支撑时怎么办呢？

加服务器加负载均衡，架构就变成这样了：

![Crepe](/img/microservice/p002.png)

### model 3

后面发现把静态文件独立出来，

通过CDN等手段进行加速，可以提升应用的整体相应，

单体应用的架构就变成

![Crepe](/img/microservice/p003.png)

### strength

传统的Web application 架构非常简单,一个实例继承了一个系统的所有功能,

通过负载均衡/设备实现多实例调用。

这种架构的好处是易开发,易调试,易部署。

适用于小型项目早期,快速开发,快速形成产品。

### shortcoming

![Crepe](/img/microservice/p005.png)

上面3中架构都还是单体应用，只是在部署方面进行了优化，所以避免不了单体应用的根本的缺点：

代码臃肿，应用启动时间长；

回归测试周期长，修复一个小小bug可能都需要对所有关键业务进行回归测试。

应用容错性差，某个小小功能的程序错误可能导致整个系统宕机；

伸缩困难，单体应用扩展性能时只能整个应用进行扩展，造成计算资源浪费。

开发协作困难，一个大型应用系统，可能几十个甚至上百个开发人员，大家都在维护一套代码的话，代码merge复杂度急剧增加。

![Crepe](/img/microservice/p006.png)

![Crepe](/img/microservice/p013.png)

## Microservice application

### Monolithic vs Microservice

![Crepe](/img/microservice/p008.png)

![Crepe](/img/microservice/p010.png)

### What kind of service is microservice?

什么样的服务才算微服务呢？

单一职责的。一个微服务应该都是单一职责的，这才是“微”的体现，一个微服务解决一个业务问题（注意是一个业务问题而不是一个接口）。

面向服务的。将自己的业务能力封装并对外提供服务，这是继承SOA的核心思想，一个微服务本身也可能使用到其它微服务的能力。

我觉得满足以上两点就可以认为典型的微服务。

![Crepe](/img/microservice/p009.png)

### microservice architecture

#### Service registry

![Crepe](/img/microservice/p007.png)

#### Configuration Center

![Crepe](/img/microservice/p011.png)


### summary

Microservices每一个业务/模块有独立的实例和数据库.将原来巨大的单体应用拆分为多个独立的service。本质上是解耦,降低复杂度。

每一个服务可以独立部署发布,发布效率更高。

开发效率更高和团队协作更加容易。

错误或异常影响范围降低,不至于牵一发而动全身。

容易接受新的技术或框架。

适用于敏捷方式快速迭代和交付有价值的产品。

没有银弹,微服务的缺点

分布式系统对于开发运维和测试人员会增加复杂度。当然这也是一种挑战。

### microservice framework

#### Spring Cloud

![Crepe](/img/microservice/p012.png)

#### Dubbo

![Crepe](/img/microservice/p016.png)

![Crepe](/img/microservice/p017.png)

![Crepe](/img/microservice/p015.png)

#### openshift

![Crepe](/img/microservice/p014.png)

日志 
EFK（ElasticSearch - Fluentd - Kibana）
~~~
Fluentd 作为日志代理，在每个节点上负责日志收集。其官网为 https://www.fluentd.org/
ElasticSearch 负责日志集中存储。其官网为 https://www.elastic.co/products/elasticsearch
Kibana 负责日志展示和查询。用户可以通过浏览器访问。其官网为 https://www.elastic.co/products/kibana
~~~

![Crepe](/img/microservice/p019.png)

![Crepe](/img/microservice/p020.png)

![Crepe](/img/microservice/p021.png)

监控
~~~
Prometheus
Grafana
~~~
reference from [https://johnnytbz.github.io/2020-06-09-monitoring-technology](https://johnnytbz.github.io/2020-06-09-monitoring-technology)

Kong Api Gateway
~~~
Rate-Limiting
Authentication
Caching
Logging
Transformations
~~~

![Crepe](/img/microservice/p022.png)

![Crepe](/img/microservice/p023.png)

![Crepe](/img/microservice/p024.png)

Kubernetes

![Crepe](/img/microservice/p018.png)

Testing
~~~
BDD - JBehave / Cucumber   
AUto testing - robot framework 
~~~
~~~
BDD example:
Given the ATM has $250
And my balance is $200
When I withdraw $150
Then the ATM has $100
And my balance is $50
~~~
reference from [https://johnnytbz.github.io/2020-03-13-robot-framework-test-locally](https://johnnytbz.github.io/2020-03-13-robot-framework-test-locally)

JWT -- JSON WEB TOKEN