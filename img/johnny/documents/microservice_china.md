
### model 1

In the “old” days when the concept of Microservice was not proposed,
a software application tended to develop and package all the features of the application,
as was often the case with a B/S application architecture

要理解什么是微服务，那么可以先理解什么是单体应用，
在没有提出微服务的概念的“远古”年代，一个软件应用，往往会将应用所有功能都开发和打包在一起，
那时候的一个B/S应用架构往往是这样的


### model 2
What happens when user traffic becomes so large that a server cannot support it?
With servers and load balancing, the architecture becomes like this

当用户访问量变大导致一台服务器无法支撑时怎么办呢？
加服务器加负载均衡，架构就变成这样了：

### model 3
Later found that the static files independent, through CDN and other means to accelerate,
can enhance the overall corresponding application,
the architecture of the monolith application becomes

后面发现把静态文件独立出来，
通过CDN等手段进行加速，可以提升应用的整体相应，
单体应用的架构就变成：

### summary
The traditional Web application architecture is very simple,
one instance contains all the business modules,
such as online shopping mall an instance has order, billing, account, courier, warehouse etc..
The benefit of this architecture is that it is very simple to develop, test, and deploy.
Suitable for early, rapid development and rapid product formation in small projects.

传统的Web application 架构非常简单,一个实例包含了所有业务模块,
比如在线商城的实例有order,billing,account,courier(快递),warehouse(仓储) etc.。
这种架构的好处是开发,测试,部署非常简单。
适用于小型项目早期,快速开发,快速形成产品。

### shortcoming
The architecture in the above 3 is still a monolithic application,
but is optimized for deployment,
so the fundamental disadvantages of monomer applications cannot be avoided:
The code is bloated and the app takes a long time to start;
Regression testing cycles are long, and fixing a small bug may require regression testing for all critical businesses.
Application fault tolerance is poor, a small function of the program error may cause the entire system down;
Scaling is difficult, and monomer applications can only scale the entire application when scaling performance, resulting in a waste of computing resources.
Development collaboration difficulties, a large application system, perhaps dozens or even hundreds of developers, everyone is maintaining a set of code, the complexity of the code has increased dramatically.

上面3中架构都还是单体应用，只是在部署方面进行了优化，所以避免不了单体应用的根本的缺点：

代码臃肿，应用启动时间长；
回归测试周期长，修复一个小小bug可能都需要对所有关键业务进行回归测试。
应用容错性差，某个小小功能的程序错误可能导致整个系统宕机；
伸缩困难，单体应用扩展性能时只能整个应用进行扩展，造成计算资源浪费。
开发协作困难，一个大型应用系统，可能几十个甚至上百个开发人员，大家都在维护一套代码的话，代码merge复杂度急剧增加。

### What kind of service is microservice
Single responsibility. A microservice should be a single responsibility, which is the embodiment of “micro”, a microservice to solve a business problem (note that it is a business problem rather than an interface).
Service-oriented. Encapsulating and delivering services to the outside world is the core idea of inheriting SOA, and a microservice itself may be able to use other microservices.
I think meeting these two points can be considered typical microservices.

什么样的服务才算微服务呢？

单一职责的。一个微服务应该都是单一职责的，这才是“微”的体现，一个微服务解决一个业务问题（注意是一个业务问题而不是一个接口）。
面向服务的。将自己的业务能力封装并对外提供服务，这是继承SOA的核心思想，一个微服务本身也可能使用到其它微服务的能力。
我觉得满足以上两点就可以认为典型的微服务。

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

Microservices每一个业务/模块有独立的实例和数据库.将原来巨大的单体应用拆分为多个独立的service。本质上是解耦,降低复杂度。

每一个服务可以独立部署发布,发布效率更高。
开发效率更高和团队协作更加容易。
错误或异常影响范围降低,不至于牵一发而动全身。
容易接受新的技术或框架。
适用于敏捷方式快速迭代和交付有价值的产品。
没有银弹,微服务的缺点

分布式系统对于开发运维和测试人员会增加复杂度。当然这也是一种挑战