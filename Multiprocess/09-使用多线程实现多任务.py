# 1. 导入线程模块
# 2. 创建线程对象
# 3. 启动线程并执行任务
import time
'''
导入线程模块
'''
import threading

def sing():
    for i in range(3):
        print("Sing...")
        time.sleep(1)

def dance():
    for i in range(3):
        print("Dance...")
        time.sleep(1)

if __name__ == '__main__':
    '''
    创建子线程并指定执行的任务
    sub_thread = threading.Thread(target=任务名)
    '''
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()