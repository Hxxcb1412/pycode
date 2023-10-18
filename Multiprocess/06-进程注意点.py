import time
import multiprocessing

def work():
    # 子进程工作2秒
    for i in range(10):
        print("working...")
        time.sleep(0.2)

if __name__ == '__main__':
    '''为了保证子进程能够正常的运行，主进程会等所有的子进程执行完成以后再销毁'''
    work_process = multiprocessing.Process(target=work)

    # 主进程睡眠1秒
    work_process.start()
    time.sleep(1)
    print("work finish...")

