---
layout: post
title: Kong API Gateway
subtitle: Kong is a cloud-native, fast, scalable, and distributed Microservice Abstraction Layer
tags: [technology]
comments: false
---
# What is Kong?

  - Kong is a cloud-native, fast, scalable, and distributed Microservice Abstraction Layer (also known as an API Gateway or API Middleware). 

  - Kong was made available as an open-source project in 2015.


![Crepe](/img/kong/p001.png)

[https://konghq.com/kong/](https://konghq.com/kong/)

# Why Kong?

### The Redundant old way
![Crepe](/img/kong/p002.png)

  - Common functionality is duplicated across multiple services
  - Systems tends to be monolithic and hard to maintain
  - Difficult to expand without impacting other services
  - Productively is inefficient because of system constraints

### The Kong way
![Crepe](/img/kong/p003.png)

  - Provide a consistent and unified interface for clients to interact with your system and a central point for managing requests and responses.
  - Decouple the complexity of the backend system from the outward-facing API that clients interact with.
  - Manage encryption of communications between clients and within the system.
  - Development teams can deliver changes more quickly than with a monolithic design

### Spring Cloud Gateway vs Kong

**Spring Cloud Gateway**
  - Inflexible: routes are configured in yml or annotated  to be RouteLocator in a Bean.
   - Need to be restarted when config is modified.


**Kong**
  - Some plugins are preset
  - Dynamic routing based on Nginx
  - Dynamic route, do not need to be restarted
  - Visible dashboard
  - High performance

### Advantages of Kong

  ![Crepe](/img/kong/p009.png)

### Kong plugins

![Crepe](/img/kong/p004.png)

[https://docs.konghq.com/hub/](https://docs.konghq.com/hub/)


# How Kong works?

### Kong installation

  - Download and get installation guideline: [https://konghq.com/install/](https://konghq.com/install/)

  ![Crepe](/img/kong/p005.png)

  ![Crepe](/img/kong/p006.png)

### Expose your Services with Kong

**Service**
 A Service is an entity representing an external upstream API or microservice
**Route**
Routes determine how (and if) requests are sent to their Services after they reach Kong Gateway. A single Service can have many Routes.
**Upstream**
Describes how incoming requests will be proxied or load balanced, represented by a virtual hostname
**Target**
Represents the services are implemented and served, identified by a hostname (or an IP address) and a port. Note that targets of every upstream can only be added or disabled. A history of target changes is maintained by the upstream

### Admin API  to Expose Your Services

**Create an upstream**
~~~

curl -X POST http://localhost:18001/upstreams \
--data "name=summer" \
--data 'healthchecks.active.healthy.interval=10'

~~~

**Create 2 targets for the upstream**
~~~

curl -X POST http://localhost:18001/upstreams/summer/targets \
--data "target=ip1:port" \
--data "weight=100"

curl -X POST http://localhost:18001/upstreams/summer/targets \
--data “target=ip2:port" \
--data "weight=100"

~~~

**Create a service**
~~~

curl -X POST  http://localhost:18001/services \
--data "name=your service name" \
--data "host=your upstream name" \
--data "path=your backend service API"

~~~

**Create a route**
~~~

curl -X POST http://localhost:18001/services/myPsaService/routes \
--data "paths[]=API that is exposed to Kong, such as, /mac/rest/v1/"

~~~

**Validate the configuration**
~~~

curl -i -X GET --url http://kong_server_ip:18000/mac/rest/v1/employee/getList

~~~

**Enable some plugins on services or routes**
~~~

curl -X POST http://localhost:18001/services/myPsaService/plugins \
    --data "name=rate-limiting" \
    --data "config.second=10"  \
    --data "config.minute=120“

curl -X POST http://localhost:18001/services/myPsaService/plugins \
    --data "name=ip-restriction" \
    --data "config.blacklist[]=ip1"

~~~

# How Kong Monitor?

### Kong + Prometheus + Grafana

  ![Crepe](/img/kong/p007.png)

  - Kong
    Prometheus plugin
  - Prometheus
   Enable Kong as a target
  - Grafana
Support Prometheus as a data source
Kong supply official dashboard to Grafana to display metrics

**Enable Prometheus plugin in Kong**
~~~

curl -i -X POST --url http://localhost:18001/plugins 
--data "name=prometheus"

~~~

**Install Prometheus Server, update prometheus.yml, add Kong's url to targets.**
~~~

static_configs:
- targets: ['localhost:9090’,’192.168.0.1:18001','192.168.0.2:18001']

~~~

**Install Grafana Server. Create a Prometheus data source on Grafana Portal. Create a dashboard for Kong on Grafana Portal. 7424 is the official dashboard provided by Kong**

  ![Crepe](/img/kong/p008.png)