package com.yooop.netty.simple;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.CharsetUtil;

/**
 * 1.我们自定义一个handler，需要继承Netty绑定好的一个HandlerAdapter
 */
public class NettyServerHandler extends ChannelInboundHandlerAdapter {

    //读取数据：此方法可以读取客户端发送的消息

    /**
     * @param ctx ：上下文对象，含有pipline，channel，地址信息
     * @param msg ；就是客户端发送的数据，默认Object
     * @throws Exception
     */
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        System.out.println("server ctx=" + ctx);

        //将msg转为ByteBuf（Netty提供的）：区别于NIO的ByteBuffer
        ByteBuf buf = (ByteBuf) msg;
        System.out.println("client send msg: " + buf.toString(CharsetUtil.UTF_8));
        System.out.println("client address: " + ctx.channel().remoteAddress());

    }

    //数据读取完毕后的处理
    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) throws Exception {

        //writeAndFlush: write+flush，将数据写入缓冲并刷新
        //一般，我们需要对发送的数据进行编码
        ctx.writeAndFlush(Unpooled.copiedBuffer("hello client!", CharsetUtil.UTF_8));
    }

    //处理异常：一般关闭通道
    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        ctx.close();
    }
}
