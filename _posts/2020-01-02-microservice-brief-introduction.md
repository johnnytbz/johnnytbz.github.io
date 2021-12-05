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

In the "old" days when the concept of Microservice was not proposed, 

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

![Crepe](/img/microservice/p013.png)

## Microservice application

### Monolithic vs Microservice

![Crepe](/img/microservice/p008.png)

![Crepe](/img/microservice/p010.png)

### What kind of service is microservice?

  - Single responsibility. A microservice should be a single responsibility, which is the embodiment of "micro", a microservice to solve a business problem (note that it is a business problem rather than an interface).
  - Service-oriented. Encapsulating and delivering services to the outside world is the core idea of inheriting SOA, and a microservice itself may be able to use other microservices.

I think meeting these two points can be considered typical microservices.

![Crepe](/img/microservice/p009.png)

### microservice architecture

#### Service registry

![Crepe](/img/microservice/p007.png)

#### Configuration Center

![Crepe](/img/microservice/p011.png)

#### A typical microservice architecture

![Crepe](/img/microservice/p012.png)


### summary

Microservice has separate instances and databases for each business/module. 

Split the original huge monomer application into separate services. 

It is essentially decoupling, reducing complexity.

Each service can be deployed independently and published more efficiently.

More efficient development and easier teamwork.

Errors or anomalies have a reduced range of influence, so as not to move the whole body in one shot.

Easy to accept new technologies or frameworks.

Ideal for rapid iteration and delivery of valuable products in agile ways.

No silver bullets, microservice disadvantages

Distributed systems add complexity to the development of operations and testers. Of course, this is also a challenge.