import time
import threading

def dance():
    for i in range(5):
        time.sleep(1)
        print('dancing...', i)

def sing():
    for i in range(5):
        time.sleep(1)
        print('singing...', i)

'''
一旦程序开启，默认就会有一个主进程
主进程里默认就会有一个主线程
'''


if __name__ == '__main__':
    # 单进程 需要10秒完成
    # 最少有一个进程 这个进程中最少有一个线程
    # 多线程 需要5秒完成（提升执行的效率）

    # （注意点！！！）
    # 三个进程：1个主进程，2个子进程

    # 2 创建子进程
    # Process :
    # target : 指定执行的任务名（函数名）

    dance_thread = threading.Thread(target=dance)
    sing_thread = threading.Thread(target=sing)

    # 3 开始子进程（如果不开启是不会执行子进程的）
    dance_thread.start()
    sing_thread.start()


