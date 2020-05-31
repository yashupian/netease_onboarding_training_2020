# python学习笔记

之前有学习python3.6的基础，学习的内容重心比较偏向于自己的学术研究，主要包括：python基础语法、python几个重要的库的学习（numpy、pandas、matplotlib）、两个深度学习框架学习（tensorflow、pytorch）。这里将根据学习要求，有针对性复习和学习。



## 1. python语言的介绍

### 1.1 python介绍

python是一种解释性、编译性、互动性和面向对象的脚本语言。

### 1.2 python的优缺点

优点：

- 简单、易学、免费开源
- 高级语言：不用管复杂的低层细节
- 可移植性、可扩展性、面向对象
- 丰富的库和规范的代码书写

缺点：

- 运行速度明显低于c++等语言
- python的架构太多



## 2.python的环境搭建

说明：

- 使用pycharm开发环境
- 搭建python2.7和3.x的环境

### 1.1 下载相关的安装文件

python-2.7.9.amd64.msi

### 2.2 安装python2.7

直接双击安装，注意选择安装路径

### 2.3 pycharm里面配置python2.7

- file>setting>Project Interpreter>show all..>+

![](../images/1590935533(1).png)

- 通过Virtualenv Environment选项创建python2.7环境并应用与项目

![](../images/1590935708(1).png)

- 点击OK即可。这时，pycharm会自动安装好相应的pip等插件，可在terminal进行测试

![](../images/1590935848(1).png)

- 使用同样的方法，也可以搭建好python3.6、python3.7版本的python环境，各个环境之间相互独立，互不影响。

## 3. python基本语法学习

### 3.1 基本语法

这部分比较基础，内容也比较多，后续慢慢补充完善。基本语法的学习包括：

- 语法基础
- 条件和循环
- break、continue和pass
- 字符串
- 列表、元组和字典
- 函数
- 模块
- I/O操作

### 3.2 技巧性内容积累

**001.python中的if-else判断**

- 常规：

```python
x = 1
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')
```

- 高级：python 中并没有类似 condition ? value1 : value2 三目操作符，但可以通过 if-else 的行内表达式完成类似的功能。

```python
worked = True
result = 'done' if worked else 'not yet'
print(result)
```

**002.python中的函数默认参数**

- 常规：函数声明只需要在需要默认参数的地方用 = 号给定即可, 但是要注意所有的默认参数都不能出现在非默认参数的前面。

```python
# 定义：
def function_name(para_1,...,para_n=defau_n,..., para_m=defau_m):
    expressions

def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print('price', price,
          'color', color,
          'brand', brand,
          'is_second_hand', is_second_hand,)
    
# 调用：
sale_car(1000)
sale_car(1000, ‘red’, ‘carmy’, True)
sale_car(1000, ‘red’, ‘carmy’, False)
# 注意，1，2两种方式等价，第3种修改了函数部分的默认参数
```

- 高级：

```python
# 1.自调用（比如单元测试）
if __name__ == '__main__':
    #code_here
 
# 2.可变参数
# 注意参数顺序：特定参数 默认参数 可变参数
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)

# 调用
report(‘Mike’, 8, 9, 10)		# 结果：Mike total grade is 27
# 说明：函数report定义了一个函数，传入一个参数为name, 后面的参数grades使用了*修饰，表明该参数是一个可变参数，这是一个可迭代的对象。

# 3.关键字参数
# 关键字参数可以传入0个或者任意个含参数名的参数，这些参数名在函数定义中并没有出现，这些参数在函数内部自动封装成一个字典(dict).
def portrait(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k, v)
```

## 4. python2.7与python3.x

### 4.1 python2.7与python3.6的对比

语法对比

| python2.7                                                    | python3.7                                                    |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| print函数用双引号                                            | print函数括号内双引号                                        |
| print 不换行使用","实现                                      | print 不换行使用end=""                                       |
| input函数：使用raw_input()接收string，input()接收数字int和float | 使用input()，可以接收任意的数据格式，相当于2.7中raw_input()和input()的合并 |
| 使用函数cmp()进行两个对象的比较                              | 已经删掉cmp()函数，比较通过operator.eq()实现                 |
| Python2 的默认编码是 asscii                                  | Python 3 默认采用了 UTF-8 作为默认编码                       |
| 后续遇到补充                                                 |                                                              |

语法对比的说明和其他的变化：

- **默认编码**：Python2 的默认编码是 asscii，这也是导致 Python2 中经常遇到编码问题的原因之一，至于是为什么会使用 asscii 作为默认编码，原因在于 Python这门语言诞生的时候还没出现 Unicode。Python 3 默认采用了 UTF-8 作为默认编码，因此python3开始不再需要在文件顶部写 # coding=utf-8。
- **迭代器：**Python2 中很多返回列表对象的内置函数和方法在 Python 3 都改成了返回类似于迭代器的对象，因为迭代器的惰性加载特性使得操作大数据更有效率。比如：Python2 中的 range 和 xrange 函数合并成了 range，如果同时兼容2和3；字典对象的 dict.keys()、dict.values() 方法都不再返回列表，而是以一个类似迭代器的 "view" 对象返回。
- **print**：在python2.7中是一个语句，在3.x中是一个接收参数的函数
- **1/2**：在python2.7中，结果为0；在3.x中结果为0.5
- **python3 彻底废弃了 long+int**，统一为int , 支持高精度整数运算
- **字符串**：python2.7的字符串有两种类型，unicode表示文本字符串，str表示字节序列；python3中对二者进行了严格的区分，用 str 表示字符串，byte 表示字节序列。
- **python3.x新增模块**：concurrent.futures、venv、unittest.mock、asyncio、selectors、typing
- **python3.x去掉的模块核函数**：gopherlib、md5、contextlib.nested、inspect.getmoduleinfo等。

代码实践：

```python
# 1.print
print "Hello Python"		# python2.7
print("Hello Python")		# python3.7

# 2.print换行
x = "a"
y = "b"
print x,
print y     # python2.7

print(x, end="")
print(y)    # python3.7

# 3.cmp()在3.7的替换：使用operator模块实现
import operator
operator.eq('hello', 'name')	# False
operator.eq('hello', 'hello')	# True
```

## 5. python连接数据库

Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口，python的这个数据库接口可以支持多种数据库，包括mysql、oracle等等。

### 5.1 python连接数据库的过程

- 引入 API 模块
- 获取与数据库的连接
- 执行SQL语句和存储过程
- 关闭数据库连接

说明：python2.7中使用mysqldb，而3.x版本使用PyMySQL

### 5.2 python连接mysql的实践（以python3为例）

- 安装PyMySQL

```python
pip install PyMySQL
```

- 连接mysql的实践（使用with语法简化操作）

```python
import pymysql

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标        
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()


if __name__ == '__main__':
    with DB(user='root', passwd='1234', db='python_db') as db:
        db.execute('select * from language')
        print(db)
        for i in db:
            print(i)
```

说明：

1).先准备好mysql数据库：建好数据库python_db并添加表格language：

![](../images/1590941326(1).png)

2).使用上述脚本查询

3).查询结果打印输出

![](../images/1590941393(1).png)

其他的数据库增删改操作基本类似，主要是sql语句的不同

```python
db.execute('SQL code')
```

