import threading
import time

def task():
    time.sleep(1)
    # current_thread : 获取当前线程的线程对象
    thread = threading.current_thread()
    # 通过thread对象可以知道线程的相关信息，例如被创建的顺序
    print(thread)

if __name__ == '__main__':
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()

# 结论：多线程之间执行是无序。
