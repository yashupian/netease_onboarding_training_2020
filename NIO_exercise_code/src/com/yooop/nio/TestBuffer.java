package com.yooop.nio;

import org.junit.Test;

import java.nio.Buffer;
import java.nio.ByteBuffer;

/**
 * 缓冲区：在Java NIO中负责数据的存取。
 * 缓冲区师数组，有7种不同类型：ByteBuffer、CharBuffer、ShortBuffer、IntBuffer、LongBuffer、FloatBuffer、DoubleBuffer
 * 上述缓冲区管理方式几乎一致，通过allocate()获取缓冲区
 */
public class TestBuffer {
    @Test
    public void test1() {

        //1.分配缓冲区:capacity()
        ByteBuffer buf = ByteBuffer.allocate(1024);

        System.out.println("-----------capacity()----------");
        System.out.println(buf.position());//0
        System.out.println(buf.limit());//1024
        System.out.println(buf.capacity());//1024

        //2.写:put()
        String str = "abcde";
        buf.put(str.getBytes());

        System.out.println("-----------put()----------");
        System.out.println(buf.position());//5
        System.out.println(buf.limit());//1024
        System.out.println(buf.capacity());//1024

        //3.切换到读：flip()
        buf.flip();
        System.out.println("-----------flip()----------");
        System.out.println(buf.position());//0
        System.out.println(buf.limit());//5
        System.out.println(buf.capacity());//1024

        //4.读取：get()
        byte[] dst = new byte[buf.limit()];
        buf.get(dst);
        System.out.println(new String(dst, 0, dst.length));

        System.out.println("-----------get()----------");
        System.out.println(buf.position());//5
        System.out.println(buf.limit());//5
        System.out.println(buf.capacity());//1024

        //5.rewind()：可重复读，回到读模式的状态
        buf.rewind();
        System.out.println("-----------rewind()----------");
        System.out.println(buf.position());//0
        System.out.println(buf.limit());//5
        System.out.println(buf.capacity());//1024

        //6.clear()：清空缓冲区，回到最初状态（但是缓冲区中的数据依然还在，处于被遗忘状态：各指针复原）
        buf.clear();
        System.out.println("-----------clear()----------");
        System.out.println(buf.position());//0
        System.out.println(buf.limit());//1024
        System.out.println(buf.capacity());//1024

        //还是有数据的
        System.out.println((char)buf.get());

    }

    @Test
    public void test2(){
        String str = "abcde";
        ByteBuffer buf = ByteBuffer.allocate(1024);

        buf.put(str.getBytes());

        buf.flip();

        byte[] dst = new byte[buf.limit()];
        buf.get(dst, 0, 2);
        System.out.println(new String(dst, 0, 2));
        System.out.println(buf.position());//2

        //mark
        buf.mark();//position=2

        buf.get(dst, 2, 2);
        System.out.println(new String(dst, 2, 2));
        System.out.println(buf.position());//4

        //reset
        buf.reset();
        System.out.println(buf.position());//2

        //判断缓冲区是否还有剩余数据
        if(buf.hasRemaining()){

            //如果有，获取缓冲区中可以操作的数量
            System.out.println(buf.remaining());//limit-position
        }
    }

    @Test
    public void test3(){
        //使用直接缓冲区
        ByteBuffer buf = ByteBuffer.allocateDirect(1024);

        //...
    }

}
