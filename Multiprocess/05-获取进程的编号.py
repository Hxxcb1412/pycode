# 1. 导入进程包  import  multiprocessing
# 2. 使用进程类创建进程对象    sub_process = multiprocessing.Process(target=任务名)
# 3. 使用进程对象启动进程执行指定任务   sub_process.start()

# 1. 导入进程包
import  multiprocessing
import time
import os

'''
获取当前进程编号：os.getpid()
获取当前父进程编号：os.getppid()
'''

def sing(num, name):
    print("pid of process sing:", os.getpid())
    print("ppid of process sing:", os.getppid())
    for i in range(num):
        print(name)
        print("Sing...")
        time.sleep(0.5)

def dance(num, name):
    print("pid of process dance:", os.getpid())
    print("ppid of process dance:", os.getppid())
    for i in range(num):
        print(name)
        print("Dance...")
        time.sleep(0.5)

'''主进程'''
if __name__ == '__main__':
    print("pid of process main", os.getpid())
    # 2. 使用进程类创建进程对象
    # target：制定进程执行的函数名
    # args：使用元祖方式给指定任务传参
    #       元组的元素顺序就是任务的参数顺序
    # kwargs：使用字典方式给指定任务传参
    #       key名就是参数的名字
    '''1.创建子进程对象并制定执行的任务名'''
    sing_process = multiprocessing.Process(target=sing, args=(3, "shido"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 2, "name": "playmaker"})
    # 3. 使用进程对象启动进程执行指定任务
    '''2. 启动子进程并执行任务'''
    sing_process.start()
    dance_process.start()

