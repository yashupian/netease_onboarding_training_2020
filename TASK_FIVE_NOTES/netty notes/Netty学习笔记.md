# Netty学习笔记

## 1.从IO到NIO到Netty

### IO

java最原始的IO通信，是阻塞的，效率低下。

### NIO

Java 1.4 引入了非阻塞 API 在 java.nio 包（NIO），其中的Selector机制是Java 的无阻塞 I/O 实现的关键。

N：new（新的）	Nonblocking（非阻塞的）

Selector机制下的NIO原理图：

![](../images/1593358996(1).png)

### Netty

Netty 是一个更为广泛使用的 Java 网络编程框架，相比NIO，他的功能更为强大。

Netty技术的特点：

- 设计
  - 针对多种传输类型的统一接口 - 阻塞和非阻塞
  - 简单但更强大的线程模型
  - 真正的无连接的数据报套接字支持
  - 链接逻辑支持复用
- 易用性
  - 大量的 Javadoc 和 代码实例
  - 除了在 JDK 1.6 + 额外的限制。（一些特征是只支持在Java 1.7 +。可选的功能可能有额外的限制。）
- 性能
  - 比核心 Java API 更好的吞吐量，较低的延时
  - 资源消耗更少，这个得益于共享池和重用
  - 减少内存拷贝
- 健壮性
  - 消除由于慢，快，或重载连接产生的 OutOfMemoryError
  - 消除经常发现在 NIO 在高速网络中的应用中的不公平的读/写比
- 安全
  - 完整的 SSL / TLS 和 StartTLS 的支持
  - 运行在受限的环境例如 Applet 或 OSGI
- 社区
  - 发布的更早和更频繁
  - 社区驱动

## 2.Netty模型

**Netty工作原理示意图（简单版）**：

![](../images/1593359320(1).png)

说明：

![](../images/1593359433(1).png)

**Netty工作原理示意图（详细版）:**

![](../images/1593359556(1).png)

说明：

![](../images/1593359613(1).png)

![](C:\Users\YP\AppData\Roaming\Typora\typora-user-images\image-20200628235424003.png)