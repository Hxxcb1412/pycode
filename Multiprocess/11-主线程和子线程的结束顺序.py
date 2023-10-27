import time
import threading

def work():
    for i in range(10):
        print('working...')
        time.sleep(1)

if __name__ == '__main__':

    # sub_thread = threading.Thread(target=work)
    # sub_thread.start()

    # 主线程结束不想等待子线程结束再结束，可以设置子线程守护主线程
    # 1. sub_thread = threading.Thread(target=work, daemon=True)
    # 2. 线程对象.setDaemon(True)
    sub_thread = threading.Thread(target=work, daemon=True)
    sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程等待1s,后结束
    time.sleep(1)
    print('主线程结束了...')

# 结论：主线程会等待所有的子线程执行结束再结束
