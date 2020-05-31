# debian系统上安装mysql和redis

说明：

- docker安装在win10宿主机上

- 使用docker安装debian等系统环境

## 1. debian镜像的拉取和实例化容器运行

```python
docker images		# 查看本地镜像
docker search debian	# 搜索远程镜像
docker pull debian		# 拉取相关的系统镜像到本地
docker images		# 再次查看本地镜像
docker run -it debian		# 以交互模式启动debian容器
```

## 2. 在启动的容器内安装一些必要的工具

```python
# 安装git
git --version  # 查看git是否可用：发现没有装
apt update
apt install git
git --version	# 验证安装

# 安装sudo命令
su		# 进入超级用户
apt-get install sudo	# sudo命令安装
adduser yp sudo		# 将我的用户名添加到sudo组内
# 配置sudoers文件
sudo ls		# 验证安装
```

## 3.在启动的debian容器内安装mysql

说明：使用deb离线包进行安装

```python
# 下载好合适的版本mysql安装包：version-specific-package-name.deb
sudo dpkg -i /PATH/version-specific-package-name.deb
sudo apt-get update
sudo apt-get install mysql-server

# 验证：
mysql -u root -p	# 之后输入安装过程设置的用户名、密码进行验证。
```

## 4. 在启动的debian容器内安装redis

```python
# 第一步下载文件到该目录  
cd /usr/local/src
wget http://download.redis.io/releases/redis-3.0.1.tar.gz
# 解压
tar xzf redis-3.0.1.tar.gz

# 第二步编译安装
make
make all
make install

# 注意：需要提前安装好make和gcc
#   安装make命令  apt-get install make
#   安装sysv-rc-conf命令  apt-get install sysv-rc-conf
#   安装升级vim命令  apt-get install vim
#   安装GCC:  apt-get install gcc

# 第三步
# 建立文件夹
mkdir /usr/redis


# 将/usr/local/bin 文件下的文件拷贝到 建立的文件夹
ls
#redis-benchmark  redis-check-aof  redis-check-dump  redis-cli  redis-sentinel  redis-server
cp redis-benchmark  /usr/redis
cp redis-check-aof /usr/redis
cp redis-check-dump  /usr/redis
cp redis-cli  /usr/redis
cp redis-sentinel  /usr/redis
cp redis-server  /usr/redis


# 将/usr/local/src/redis-3.0.1目录中 解压出的文件的redis.conf拷贝到 /usr/redis
cp redis.conf /usr/redis

# 第四步.
# 启动服务
# 进入/usr/redis目录
# 启动命令：redis-server redis.conf 
# 关闭命令：建议在客户端停止 shutdown

# 第五步
# 注册服务，设置开机启动

# 将/usr/local/src/redis-3.0.1/utils/   redis_init_script     文件下的文件拷贝到 /etc/init.d/ 并且重命名为redisd

cp /usr/local/src/redis-3.0.1/utils/redis_init_script  /etc/init.d/redisd

# 修改文件redisd

# chkconfig:2345 10 90

REDISPORT=6379
EXEC=/usr/redis/redis-server
CLIEXEC=/usr/redis/redis-cli

PIDFILE=/var/run/redis.pid
CONF="/usr/redis/redis.conf"

# 启动测试

/etc/init.d/redisd start

# 设置开机自启动
chkconfig redisd on
# 注意：可能会找不到命令，安装命令 apt-get install chkconfig 

# 重新启动机器
reboot

# 一些操作

# 查看redis 6379端口是否正在运行
ps aux | grep redis
# 正常停止redis-server　服务，使用reids 客户端命令: redis-cli shutdown
# 如果停止不了则采取杀死进程的方式：kill -9 PID
# 例如：kill -9 831

# 服务端启动
redis-server /usr/redis/redis.conf

# 客户端连接
redis-cli -h IP地址 -p 端口 -a 密码
redis-cli -h 127.0.0.1 -p 6379 -a yxt123

# 退出客户端
quit
```

