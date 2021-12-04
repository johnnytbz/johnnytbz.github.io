---
layout: post
title: microservice brief introduction
subtitle: How to understand micro service
tags: [technology]
comments: true
---


# What is microservices?


## Monolithic applications

### model 1

In the "old" days when the concept of microservices was not proposed, 

a software application tended to develop and package all the features of the application, 

as was often the case with a B/S application architecture

![Crepe](/img/microservice/p001.png)

### model 2

What happens when user traffic becomes so large that a server cannot support it? 

With servers and load balancing, the architecture becomes like this

![Crepe](/img/microservice/p002.png)

### model 3

Later found that the static files independent, through CDN and other means to accelerate, 

can enhance the overall corresponding application, 

the architecture of the monolith application becomes

![Crepe](/img/microservice/p003.png)

### summary

![Crepe](/img/microservice/p004.png)

The traditional Web application architecture is very simple, 

one instance contains all the business modules, 

such as online shopping mall an instance has order, billing, account, courier, warehouse etc.. 

The benefit of this architecture is that it is very simple to develop, test, and deploy. 

Suitable for early, rapid development and rapid product formation in small projects.

### shortcoming

![Crepe](/img/microservice/p005.png)

The architecture in the above 3 is still a monolithic application, 

but is optimized for deployment, 

so the fundamental disadvantages of monomer applications cannot be avoided:

  - The code is bloated and the app takes a long time to start;
  - Regression testing cycles are long, and fixing a small bug may require regression testing for all critical businesses.
  - Application fault tolerance is poor, a small function of the program error may cause the entire system down;
  - Scaling is difficult, and monomer applications can only scale the entire application when scaling performance, resulting in a waste of computing resources.
  - Development collaboration difficulties, a large application system, perhaps dozens or even hundreds of developers, everyone is maintaining a set of code, the complexity of the code has increased dramatically.


![Crepe](/img/microservice/p006.png)

## microservices application

### What kind of service is microservice?

  - Single responsibility. A microservice should be a single responsibility, which is the embodiment of "micro", a microservice to solve a business problem (note that it is a business problem rather than an interface).
  - Service-oriented. Encapsulating and delivering services to the outside world is the core idea of inheriting SOA, and a microservice itself may be able to use other microservices.

I think meeting these two points can be considered typical microservices.

### A typical architecture for microservices

#### Service registry

#### Configuration Center

#### 