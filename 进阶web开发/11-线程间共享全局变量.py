import threading
import time


# 结论：由于线程是依附于进程的，一个进程中的所有的线程都是使用的同一片内存空间
# 一个进程中的,线程是共享全局变量的.
g_num = []

def my_wirte():
    global g_num

    for i in range(5):
        g_num.append(i)

    print('write:', g_num)


def my_read():
    global g_num
    print('read:', g_num)

if __name__ == '__main__':
    sub_write = threading.Thread(target=my_wirte)
    sub_read = threading.Thread(target=my_read)

    sub_write.start()
    sub_read.start()
    time.sleep(1)