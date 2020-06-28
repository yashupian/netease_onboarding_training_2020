package com.yooop.netty.simple;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;

/**
 * Netty 服务端
 */
public class NettyServer {
    public static void main(String[] args) throws Exception {

        //1.创建bossGroup和workerGroup
        //1)创建了两个线程组：bossGroup和workerGroup
        //2）bossGroup只处理连接请求，交给workerGroup处理
        //3)这两个都是在循环
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();


        try {
            //2.创建服务器的启动对象，配置参数
            ServerBootstrap bootstrap = new ServerBootstrap();
            //使用链式编程进行设置
            bootstrap.group(bossGroup, workerGroup)                       //设置两个线程组
                    .channel(NioServerSocketChannel.class)                //设置服务器端通道的实现类：NioServerSocketChannel
                    .option(ChannelOption.SO_BACKLOG, 128)          //最大客户端连接数128
                    .childOption(ChannelOption.SO_KEEPALIVE, true)  //保持活动连接状态
                    .childHandler(new ChannelInitializer<SocketChannel>() {     //客户端：SocketChannel

                        //给pipline设置处理器
                        @Override
                        protected void initChannel(SocketChannel ch) throws Exception {
                            ch.pipeline().addLast(new NettyServerHandler());
                        }
                    });

            //提示
            System.out.println("server is ready...");

            //绑定一个端口并同步，生成一个ChannelFuture对象
            //在这里就启动了服务器
            ChannelFuture cf = bootstrap.bind(6668).sync();

            //对关闭通道进行监听
            cf.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }
}
