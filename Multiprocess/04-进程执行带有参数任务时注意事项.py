# 1. 导入进程包  import  multiprocessing
# 2. 使用进程类创建进程对象    sub_process = multiprocessing.Process(target=任务名)
# 3. 使用进程对象启动进程执行指定任务   sub_process.start()

# 1. 导入进程包
import  multiprocessing
import time

def sing(num, name):
    for i in range(num):
        print(name)
        print("Sing...")
        time.sleep(0.5)

def dance(num, name):
    for i in range(num):
        print(name)
        print("Dance...")
        time.sleep(0.5)

if __name__ == '__main__':
    # 2. 使用进程类创建进程对象
    # target：制定进程执行的函数名
    # args：使用元祖方式给指定任务传参
    #       元组的元素顺序就是任务的参数顺序
    # kwargs：使用字典方式给指定任务传参
    #       key名就是参数的名字
    sing_process = multiprocessing.Process(target=sing, args=(3, "shido"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 2, "name": "playmaker"})
    # 3. 使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()

# 元组方式传参：元组方式传参一定要和参数的顺序保持一致
# 字典方式传参：字典传参字典中的key一定要和参数名保持一致
