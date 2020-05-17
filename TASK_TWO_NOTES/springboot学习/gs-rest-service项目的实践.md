# gs-rest-service项目的初实践

## 1.说明

这是springboot官网给出的一个实践案例（https://github.com/spring-guides/gs-rest-service），是一个简单的基于REST服务的web应用。



## 2.实践练习过程

- 下载项目

```xml
git clone https://github.com/spring-guides/gs-spring-boot.git
```

- 项目的导入运行和测试

![](../images/1589733810(1).png)

![](../images/1589733884(1).png)

注意：导入的时候要选中build.gradle或者pom.xml文件

- 项目结构分析

![](../images/1589734002(1).png)

其中，GreetingController是请求处理器，Greeting是一个请求响应模板，RestServiceApplication是项目的启动类，pom.xml用于maven项目的依赖管理。

- 运行实践

![](../images/1589734209(1).png)

如图，发送请求/greeting时，返回响应内容：

```json
{"id":1,"content":"Hello, World!"}
```

