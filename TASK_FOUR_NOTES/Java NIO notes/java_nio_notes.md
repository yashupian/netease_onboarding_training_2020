# java NIO笔记

## 一、关于java NIO

Java NIO（New IO）是从Java 1.4版本开始引入的 一个新的IO API，可以替代标准的Java IO API。 NIO与原来的IO有同样的作用和目的，但是使用的方式完全不同，**NIO支持面向缓冲区的、基于通道的IO操作**。NIO将以**更加高效**的方式进行文件的读写操作。

##　二、IO与NIO的对比

| IO                      | NIO                         |
| ----------------------- | --------------------------- |
| 面向流(Stream Oriented) | 面向缓冲区(Buffer Oriented) |
| 阻塞IO(Blocking IO)     | 非阻塞IO(Non Blocking IO)   |
| 无选择器                | 选择器(Selectors)           |

## 三、通道和缓冲区概念

Java NIO系统的核心在于：通道(Channel)和缓冲区 (Buffer)。

**通道（Channel）：**

- **通道**表示打开到IO设备(例如：文件、套接字)的连接。**若需要使用NIO系统，需要获取用于连接 IO 设备的通道**以及**用于容纳数据的缓冲区**。然后**操作缓冲区**，对数据进行处理。
- 总结：Channel 负责传输， Buffer 负责存储。

**缓冲区（Buffer）：**

- 一个用于特定基本数据类型的容器。由 java.nio 包定义的，所有缓冲区都是 Buffer 抽象类的子类。

- **缓冲区Buffer的作用**：主要用于与**NIO通道**进行交互，**数据是从通道读入缓冲区，从缓冲区写入通道中的**。

## 四、缓冲区（Buffer）

Buffer就像一个数组，可以保存多个相同类型的数据。boolean 除外，每一种基本数据类型都对应有Buffer的子类：**ByteBuffer（最常用）**、CharBuffer、ShortBuffer、IntBuffer、LongBuffer、FloatBuffer、DoubleBuffer。

### 4.1 缓冲区的四个核心属性

- **容量（capacity）**：表示 Buffer 最大数据容量，缓冲区容量不能为负，并且创建后不能更改；
- **限制（limit）**：第一个不应该读取或写入的数据的索引，即位于 limit 后的数据不可读写。缓冲区的限制不能为负，并且不能大于其容量。
- **位置（position）**：下一个要读取或写入的数据的索引。缓冲区的位置不能为负，并且不能大于其限制。
- **标记（mark）**：标记是一个索引，通过 Buffer 中的 mark() 方法指定 Buffer 中一个特定的 position，之后可以通过调用 reset() 方法恢复到这个 position（**即重置reset**）。

关系：0 <= mark <= position <= limit <= capacity

### 4.2 缓冲区常用方法

```java
allocate();
position();
limit();
capacity();

put();
flip();
get();
rewind();//可重复读，回到读模式的状态
clear();//清空缓冲区，回到最初状态（但是缓冲区中的数据依然还在，处于被遗忘状态：各指针复原）
mark();//标记position位置
reset();//positon回到标记的位置

//判断缓冲区是否还有剩余数据
if(buf.hasRemaining()){
    //如果有，获取缓冲区中可以操作的数量
    System.out.println(buf.remaining());//limit-position
}

```

### 4.3 直接缓冲区与非直接缓冲区

- 非直接缓冲区：allocate()创建；

- 直接缓冲区：allocateDirect() 工厂方法创建，可以提高效率。风险：占用更多物理内存资源。因此，最好仅在直接缓冲区能在程序性能方面带来明显好 处时分配它们。
- isDirect()判断缓冲区的类型

直接缓冲区为什么提高效率？

避免将缓冲区（JVM内存中）的内容复制到中间缓冲区（物理内存中）中（或从中间缓冲区中复制内容）。

![](../images/1592146602(1).png)

测试代码如下：

```java
@Test
    public void test3(){
        //使用直接缓冲区
        ByteBuffer buf = ByteBuffer.allocateDirect(1024);
        
        //...
    }
```

### 五、通道（Channel）

定义：通道（Channel）：由 java.nio.channels 包定义的。Channel 表示 IO 源与目标打开的连接。

注意：Channel 类似于传统的“流”。只不过 Channel 本身不能直接访问数据，Channel 只能与Buffer进行交互。

### 5.1 主要实现类

- FileChannel：用于读取、写入、映射和操作文件的通道。
- DatagramChannel：通过 UDP 读写网络中的数据通道。 
- SocketChannel：通过 TCP 读写网络中的数据。 
- ServerSocketChannel：可以监听新进来的 TCP 连接，对每一个新进来的连接都会创建一个 socketChannel。

### 5.2 主要的一些方法

**获取通道**

①获取通道的一种方式是对支持通道的对象调用 getChannel() 方法，支持通道的类如下：

FileInputStream、FileOutputStream、RandomAccessFile、DatagramSocket、Socket、ServerSocket

②获取通道的其他方式是使用 Files 类的静态方法 newByteChannel() 获取字节通道；

③通过通道的静态方法 open() 打开并返回指定通道。

**通道的数据传输**

将Buffer写入Channel

```java
//inChannel是通道对象
int bytesWritten = inChannel.write();
```

从Channel中读取数据到Buffer

```java
int bytesRead = inChannel.read();
```

**分散(Scatter)和聚集(Gather)**

**分散读取**（Scattering Reads）是指从 Channel 中读取的数据“分散”到多个 Buffer 中；

**聚集写入**（Gathering Writes）是指将多个 Buffer 中的数据“聚集” 到 Channel通道中；

**传输**

```java
transferFrom();//将数据从源通道传输到其他 Channel 中;
transferTo();//将数据从源通道传输到其他 Channel 中;
```

**FileChannel 的常用方法**

```java
int read(ByteBuffer dst);//从 Channel 中读取数据到 ByteBuffer
long read(ByteBuffer[] dsts);// 将 Channel 中的数据“分散”到 ByteBuffer[]
int write(ByteBuffer src);// 将 ByteBuffer 中的数据写入到 Channel
long write(ByteBuffer[] srcs);// 将 ByteBuffer[] 中的数据“聚集”到 Channel
long position();// 返回此通道的文件位置
FileChannel position(long p);// 设置此通道的文件位置
long size();// 返回此通道的文件的当前大小
FileChannel truncate(long s);// 将此通道的文件截取为给定大小
void force(boolean metaData);// 强制将所有对此通道的文件更新写入到存储设备中
```

## 六、NIO 的非阻塞式网络通信

- **传统的IO：**传统的 IO 流都是阻塞式的。也就是说，当一个线程调用 read() 或 write() 时，该线程被阻塞，直到有一些数据被读取或写入，该线程在此期间不能执行其他任务；
- **NIO：**Java NIO 是非阻塞模式的。当线程从某通道进行读写数据时，若没有数据可用时，该线程可以进行其他的任务。

### 6.1 选择器（Selector）

**选择器（Selector）** 是 SelectableChannle 对象的多路复用器，Selector 可 以同时监控多个 SelectableChannel 的 IO 状况。也就是说，利用 Selector 可使一个单独的线程管理多个 Channel。

**Selector 是非阻塞 IO 的核心。**

SelectableChannle 的结构如下图：

![](../images/1592148179(1).png)

选择器的应用（主要方法总结）：

```java
//创建选择器
Selector selector = Selector.open();

//向选择器注册通道

```

