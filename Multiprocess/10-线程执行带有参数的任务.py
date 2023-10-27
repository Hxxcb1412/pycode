
import time
import threading

def sing(num, name):
    for i in range(num):
        print(name, "Sing...")
        time.sleep(1)

def dance(count):
    for i in range(count):
        print("Dance...")
        time.sleep(1)

if __name__ == '__main__':
    # args：以元组的方式给执行任务传递参数
    # 元组方式传参：元组方式传参一定要和参数的顺序保持一致。
    sing_thread = threading.Thread(target=sing, args=(3, "Shido"))
    # kwargs：以字典方式给执行任务传递参数
    # 字典方式传参：字典方式传参字典中的key一定要和参数名保持一致
    dance_thread = threading.Thread(target=dance, kwargs={"count": 3})

    sing_thread.start()
    dance_thread.start()