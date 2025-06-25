---
layout: post
title: How to use monitoring technology in microservice projects
subtitle: monitoring using exporter prometheus grafana
tags: [technology]
comments: true
---


## what is prometheus?
    
Prometheus is an open source system monitoring and alarming framework.

It start from Google borgmon. One of CNCF (Cloud Native Computing Foundation) projects.The second project join CNCF.

Development by go language.  

for single server have strong performance: support thousands of targets, a million time series per second.

the official architecture diagram:
![Crepe](https://prometheus.io/assets/docs/architecture.svg)

TSDB using time series database store data.

Prometheus has two ways of collecting data, pull and pushgateway.

mainly the pull method, which is to obtain the index data from the specified Target at regular intervals by using the HTTP interface.


## how to using monitor in microservice?    

### 1.expose prometheus data from spring boot actuator

	using micrometer

**Pom.xml adds related package dependencies**

~~~	
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-core</artifactId>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
~~~

**add config in application.yml**

~~~
management.endpoints.enabled-by-default=false
management.endpoint.info.enabled=true
management.endpoint.health.enabled=true
management.endpoint.loggers.enabled=true
management.endpoint.metrics.enabled=true
management.endpoint.prometheus.enabled=true
management.endpoint.jolokia.enabled=true management.endpoints.web.exposure.include=info,health,loggers,metrics,prometheus,jolokia
~~~

**counter and timer in program**

A single metric means, that a Counter represents a single value, e.g. invoke rest API each time. It is monotonically increasing, so it can only increase, usually one-by-one. It is a cumulative metric, so it always contains the overall value.

**add counter for invoke API**

~~~
MeterRegistry registry = new SimpleMeterRegistry();
Metrics.addRegistry(registry);
Counter counter = Metrics.counter("http.requests.rest.counter", "action", "changeSubscriptionPackage");
counter.increment();
~~~

**add timer for invoke API request time**

~~~
MeterRegistry registry = new SimpleMeterRegistry();
Timer.Sample timer = Timer.start(registry);
// do something
timer.stop(Metrics.timer("http.requests.rest.timer", "action", "changeSubscriptionPackage"));
~~~

**You will get the following information when you request the RestAPI.**

~~~
http_requests_rest_api_counter_total{action="changeSubscriptionPackage",} 2.0
http_requests_rest_api_counter_total{action="getSubscriptionDetails",} 3.0
http_requests_rest_api_counter_total{action="changeSubscriptionState",} 1.0
http_requests_rest_api_timer_seconds_count{action="changeSubscriptionPackage",} 2.0
http_requests_rest_api_timer_seconds_sum{action="changeSubscriptionPackage",} 1.9098152
http_requests_rest_api_timer_seconds_count{action="getSubscriptionDetails",} 3.0
http_requests_rest_api_timer_seconds_sum{action="getSubscriptionDetails",} 1.1893008
http_requests_rest_api_timer_seconds_count{action="changeSubscriptionState",} 1.0
http_requests_rest_api_timer_seconds_sum{action="changeSubscriptionState",} 0.6497153	
~~~

OR using AOP to count

~~~
package com.ericsson.dcp.sica.application.util;
 
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
 
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface PrometheusTimers {
}
~~~

~~~
package com.ericsson.dcp.sica.application.util;
 
import com.ericsson.dcp.sica.application.services.MetricsService;
 
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;
 
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Metrics;
import io.micrometer.core.instrument.Timer;
import io.micrometer.core.instrument.simple.SimpleMeterRegistry;
 
@Aspect
@Component
public class PrometheusTimersAspect {
 
    String metricsName = "http.requests.rest.api";
 
    @Pointcut("@annotation(com.ericsson.dcp.sica.application.util.PrometheusTimers)")
    private void pointcut() {
    }
 
    @Around("pointcut()")
    public Object around(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();
 
        MetricsService.counterIncrement(metricsName, "action", methodName);
        MeterRegistry registry = new SimpleMeterRegistry();
        Timer.Sample timer = Timer.start(registry);
 
        Object result = joinPoint.proceed();
 
        timer.stop(Metrics.timer(metricsName + ".timer", "action", methodName));
 
        return result;
    }
 
}
~~~


## how to practice in laptop locally using docker?

create your network first, need to specify the network IP.

~~~
docker network create --subnet=172.18.0.0/16 mynetwork
~~~

**1.download images**

~~~
docker pull prom/prometheus
docker pull grafana/grafana
docker pull prom/alertmanager
docker pull prom/node-exporter
~~~

**2.launch node-exporter**

~~~
docker run -d --network mynetwork --ip 172.18.0.11 -p 9100:9100 prom/node-exporter
~~~

open in web browser, you can view the collected system information.

http://localhost:9100/metrics

![Crepe](/img/monitor/01.png)

**3.launch prometheus**

create yml file : C:\monitor\prometheus.yml

~~~
global:
  scrape_interval:     60s
  evaluation_interval: 60s
 
rule_files:
  - "rules.yml"
 
alerting:
  alertmanagers:
  - static_configs:
    - targets: ['172.18.0.5:9093']
 
scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']
        labels:
          instance: prometheus
  
  - job_name: node
    static_configs:
      - targets: ['172.18.0.11:9100']
        labels:
          instance: node
  - job_name: mysql
    static_configs:
      - targets: ['172.18.0.12:9104']
        labels:
          instance: mysql
  - job_name: sica
    metrics_path: /actuator/prometheus
    static_configs:
      - targets: ['100.98.141.205:8080']
        labels:
          instance: sica
  - job_name: alertmanager
    static_configs:
      - targets: ['172.18.0.5:9093']
        labels:
          instance: alertmanager
~~~          

create yml file : C:\monitor\rules.yml

~~~
groups:
  - name: node_alerts
    rules:
    - alert: InstanceDown    ## alert name
      expr: up{job='node'} == 0  ## alert condition
      for: 1m  ## when more than 1 min，prometheus will sent alert message to alertmanger
      labels:
        severity: "warning"
      annotations:
        summary: Host {{ $labels.instance }} of {{ $labels.job }} is Down!
  - name: sica_alerts
    rules:
    - alert: SICADown   
      expr: up{job='sica'} == 0
      for: 1m
      labels:
        severity: "warning"
      annotations:
        summary: Host {{ $labels.instance }} of {{ $labels.job }} is Down!
~~~

~~~
docker run -d --network mynetwork --ip 172.18.0.3 -p 9090:9090 -v C:\monitor\prometheus.yml:/etc/prometheus/prometheus.yml -v C:\monitor\rules.yml:/etc/prometheus/rules.yml prom/prometheus
~~~

view in web browser

http://localhost:9090/graph

![Crepe](/img/monitor/02.png)


**4.launch grafana**

create folder : C:\monitor\grafana-storage

~~~
docker run -d --network mynetwork --ip 172.18.0.4 -p 3000:3000 --name=grafana -v C:\monitor\grafana-storage:/var/lib/grafana grafana/grafana
~~~

view in web browser

http://localhost:3000/login    (default login   admin/admin)

setting grafana data sources from prometheus : http://172.18.0.3:9090

![Crepe](/img/monitor/03.png)


**5.launch alertmanager**

create yml file : C:\monitor\alertmanager.yml

~~~
global:
  smtp_smarthost: ''
  smtp_from: '***@gmail.com'
  smtp_auth_username: '***@gmail.com'
  smtp_auth_password: 'password'
  smtp_require_tls: false
  
route:
  group_interval: 1m
  repeat_interval: 1m
  receiver: 'mail-receiver'
  
receivers:
  - name: 'mail-receiver'
    email_configs:
    - to: '***@gmail.com'

~~~

~~~
docker run -d --network mynetwork --ip 172.18.0.5 -p 9030:9030 -v C:\monitor\alertmanager.yml:/etc/alertmanager/alertmanager.yml prom/alertmanager
~~~

### useful Material

[exporter](https://prometheus.io/docs/instrumenting/exporters)

[grafan dashboard template](https://grafana.com/grafana/dashboards?direction=asc&orderBy=name)
