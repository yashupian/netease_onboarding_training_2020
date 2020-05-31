# 数据库和redis的学习

## 1.数据库知识点的复习

### 1.1 数据库事务

数据库事务是指满足 ACID 特性的一组数据库操作，ACID是事务的四个特性，如下：

原子性（Atomicity）：

一致性（Consistency）：

隔离性（Isolation）：

持久性（Durability）：

### 1.2 数据库并发一致性问题

丢失修改

脏读数据

不可重复读

幻读

### 1.3 数据库的锁机制

从锁细粒度上分：行级锁、表级锁

从锁的类型上分：读(X)写(S)锁、意向锁(IX、IS)

锁的三级封锁协议：

一级：事务 T 要修改数据 A 时必须加 X 锁，直到 T 结束才释放锁

二级：在一级的基础上，要求读取数据 A 时必须加 S 锁，读取完马上释放 S 锁（解决读脏）

三级：在二级的基础上，要求读取数据 A 时必须加 S 锁，直到事务结束了才能释放 S 锁（解决不可重复读）

### 1.4 数据库隔离级别

未提交读（READ UNCOMMITTED）

提交读（READ COMMITTED）

可重复读（REPEATABLE READ）

可串行化（SERIALIZABLE）

### 1.5数据库的范式设计

第一范式 (1NF)：属性不可分

第二范式 (2NF)：每个非主属性完全函数依赖于键码

第三范式 (3NF)：非主属性不传递函数依赖于键码（去除链式的依赖）

## 2.SQL语法

注释

```sql
SELECT *
FROM mytable; -- 注释
/* 注释1
   注释2 */
```

创建数据库

```sql
CREATE DATABASE test;
USE test;
```

创建表

```sql
CREATE TABLE mytable (
  # int 类型，不为空，自增
  id INT NOT NULL AUTO_INCREMENT,
  # int 类型，不可为空，默认值为 1，不为空
  col1 INT NOT NULL DEFAULT 1,
  # 变长字符串类型，最长为 45 个字符，可以为空
  col2 VARCHAR(45) NULL,
  # 日期类型，可为空
  col3 DATE NULL,
  # 设置主键为 id
  PRIMARY KEY (`id`));
```

修改表

```sql
# 添加
ALTER TABLE mytable
ADD col CHAR(20);

# 删除列
ALTER TABLE mytable
DROP COLUMN col;

# 删除表
DROP TABLE mytable;

# 插入数据
INSERT INTO mytable(col1, col2)
VALUES(val1, val2);

# 更新数据
UPDATE mytable SET col = val WHERE id = 1;

# 删除数据
DELETE FROM mytable
WHERE id = 1;

# 查询
select

# 限制数目
limit

# 排序
ASC DESC

# 过滤
WHERE

# 分组
GROUP BY

# 其他内容：子查询、内外连接、组合查询
```

## 3.MySQL

### 3.1 索引

**B+树原理**

B+树和红黑树的对比：

- B+ 树有更低的树高

- 磁盘访问原理

- 磁盘预读特性



**mysql的索引**

B+Tree 索引和哈希索引



**索引的优点**

- 大大减少了服务器需要扫描的数据行数。
- 帮助服务器避免进行排序和分组，以及避免创建临时表（B+Tree 索引是有序的，可以用于 ORDER BY 和 GROUP BY 操作。临时表主要是在排序和分组过程中创建，不需要排序和分组，也就不需要创建临时表）。
- 将随机 I/O 变为顺序 I/O



### 3.2 查询的优化

使用 Explain 进行分析

优化数据访问

- 减少请求的数据量：最好不要使用 SELECT * 语句、使用limit
- 减少服务器端扫描的行数
- 切分大查询
-  分解大连接查询



### 3.3 数据库引擎

**InnoDB**

MySQL 默认的事务型存储引擎

四个标准的隔离级别，默认级别是可重复读

通过多版本并发控制（MVCC）+ Next-Key Locking 防止幻影读

主索引是聚簇索引



**MyISAM**

设计简单，数据以紧密格式存储

不支持事务



**二者比较：**

- 事务：InnoDB 是事务型的，可以使用 Commit 和 Rollback 语句。
- 并发：MyISAM 只支持表级锁，而 InnoDB 还支持行级锁。
- 外键：InnoDB 支持外键。
- 备份：InnoDB 支持在线热备份。
- 崩溃恢复：MyISAM 崩溃后发生损坏的概率比 InnoDB 高很多，而且恢复的速度也更慢。
- 其它特性：MyISAM 支持压缩表和空间数据索引。



## 4. Redis

Redis 是速度非常快的非关系型（NoSQL）内存键值数据库，可以存储键和五种不同类型的值之间的映射。

键的类型只能为字符串，值支持五种数据类型：字符串、列表、集合、散列表、有序集合。

数据类型总结如下：

| 数据类型 | 可以存储的值           | 操作                                                         |
| -------- | ---------------------- | ------------------------------------------------------------ |
| STRING   | 字符串、整数或者浮点数 | 对整个字符串或者字符串的其中一部分执行操作 对整数和浮点数执行自增或者自减操作 |
| LIST     | 列表                   | 从两端压入或者弹出元素 对单个或者多个元素进行修剪， 只保留一个范围内的元素 |
| SET      | 无序集合               | 添加、获取、移除单个元素 检查一个元素是否存在于集合中 计算交集、并集、差集 从集合里面随机获取元素 |
| HASH     | 包含键值对的无序散列表 | 添加、获取、移除单个键值对 获取所有键值对 检查某个键是否存在 |
| ZSET     | 有序集合               | 添加、获取、删除元素 根据分值范围或者成员来获取元素 计算一个键的排名 |

具体的代码操作（直接在win10上安装的redis）

```python
# STRING
> set hello world
OK
> get hello
"world"
> del hello
(integer) 1
> get hello
(nil)


# LIST
> rpush list-key item
(integer) 1
> rpush list-key item2
(integer) 2
> rpush list-key item
(integer) 3

> lrange list-key 0 -1
1) "item"
2) "item2"
3) "item"


# SET
> sadd set-key item
(integer) 1
> sadd set-key item2
(integer) 1
> sadd set-key item3
(integer) 1
> sadd set-key item
(integer) 0


# HASH
> hset hash-key sub-key1 value1
(integer) 1
> hset hash-key sub-key2 value2
(integer) 1
> hset hash-key sub-key1 value1
(integer) 0

> hgetall hash-key
1) "sub-key1"
2) "value1"
3) "sub-key2"
4) "value2"


# ZSET
> zadd zset-key 728 member1
(integer) 1
> zadd zset-key 982 member0
(integer) 1
> zadd zset-key 982 member0
(integer) 0

> zrange zset-key 0 -1 withscores
1) "member1"
2) "728"
3) "member0"
4) "982"
```

