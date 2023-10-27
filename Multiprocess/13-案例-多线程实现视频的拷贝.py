import os
import threading

'''使用多线程也可以实现多任务拷贝提高程序性能'''

def copy_file(file_name, source_dir, dest_dir):
    # 1. 拼接源文件路径和目标文件路径
    source_path = source_dir + '\\' + file_name
    dest_path = dest_dir + '\\' + file_name

    # 2. 打开源文件和目标文件
    with open(source_path, 'rb') as source_file:
        with open(dest_path, 'wb') as dest_file:
            # 3. 循环拷贝源文件到目标文件
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break

if __name__ == '__main__':
    # 1. 定义源目录路径和目标目录
    source_dir = 'F:\\video\\视频-python从0开始学编程\\day10视频'
    dest_dir = 'F:\\video\\aa'

    # 2. 创建目标目录
    try:
        os.mkdir(dest_dir)
    except:
        print('Exist...')

    # 3. 读取源文件
    file_list = os.listdir(source_dir)

    # 4. 遍历列表，获取需要拷贝的文件
    for file_name in file_list:

        # 5. 创建子线程实现多任务拷贝
        # copy_file(file_name, source_dir, dest_dir)
        sub_threading = threading.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_threading.start()