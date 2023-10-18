import time
import multiprocessing

def work():
    # 子进程工作2秒
    for i in range(10):
        print("working...")
        time.sleep(0.2)

if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)

    # 设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
    '''设置守护主进程方式：   子进程对象.daemon = True'''
    work_process.daemon = True

    # 主进程睡眠1秒
    work_process.start()
    time.sleep(1)
    print("work finish...")