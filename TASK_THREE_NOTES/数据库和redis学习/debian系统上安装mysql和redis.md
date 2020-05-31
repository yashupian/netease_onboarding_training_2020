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

```

```

