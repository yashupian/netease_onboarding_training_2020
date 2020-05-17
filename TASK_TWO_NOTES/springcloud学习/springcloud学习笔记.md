# springcloud学习笔记

本笔记主要参考的资料包括：

- 周阳SpringCloud2020视频课（https://www.bilibili.com/video/BV1ZW411G7Tf）
- springcloud官方教程（https://spring.io/projects/spring-cloud）
- 其他网上的一些博客资料



## 1.springcloud和springboot

springcloud：是一种分布式微服务架构的一站式解决方案，是多种微服务架构落地技术的集合体，俗称微服务全家桶。

springboot：是一种服务开发技术，是一种具体服务的开发框架



## 2.springcloud的六大神器

springcloud一共涉及到20多种技术内容，其中最为重要、最为核心的6种如下：

- **服务注册与发现：EUREKA**

- 服务负载均衡与调用：NETFLIX OSS RIBBON

- 服务负载与调用：NETTFLIX

- 服务熔断降级：HYSTRIX

- **服务网关：**Zuul/Gateway

- 服务分布式配置：SpringCloud Config



## 3.服务注册Eureka

### 3.1 是什么？

Eureka 是 Netflix 开发的，一个基于 REST 服务的，服务注册与发现的组件，以实现中间层服务器的负载平衡和故障转移，主要包括两个组件：

- Eureka Client：一个Java客户端，用于简化与 Eureka Server 的交互（通常就是微服务中的客户端和服务端）
- Eureka Server：提供服务注册和发现的能力（通常就是微服务中的注册中心）

### 3.2 Eureka 客户端与服务器之间的通信

服务发现有两种模式：一种是**客户端发现模式**，一种是**服务端发现模式**。Eureka采用的是**客户端发现模式**。

### 3.3 Eureka的架构

![](../images/1589735903(1).png)



## 4. 网关Gateway

Spring Cloud **Gateway** 是 Spring Cloud 新推出的网关框架，之前是 Netflix Zuul。

网关通常在项目中为了**简化前端的调用逻辑**，同时也**简化内部服务之间互相调用的复杂度**；具体作用就是转发服务，接收并转发所有内外部的客户端调用；其他常见的功能还有权限认证，限流控制等等。

网关的基本功能：

- 转发功能
- 熔断功能
- 限流功能
- ……

### 5.后续继续学习补充

