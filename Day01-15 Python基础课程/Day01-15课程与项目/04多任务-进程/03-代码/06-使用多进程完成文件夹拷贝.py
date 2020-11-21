import os
import multiprocessing
import time

def copy_file(src_path, file_name, dest_path, queue):
    """源目录　文件名　目的目录"""
    # demo    01.py  demo-备份

    # 打开一个源文件　读取
    src_file = open(src_path + '/' + file_name, 'rb')

    # 打开一个目标文件　写入　
    dest_file = open(dest_path + '/' + file_name, 'wb')

    file_data = src_file.read()
    dest_file.write(file_data)

    # 关闭文件
    src_file.close()
    dest_file.close()

    # 通过队列告诉主进程　我已经完成这个文件的拷贝
    queue.put(file_name)


if __name__ == '__main__':
    # 1 用户输入需要拷贝的源目录名称
    src_path = input("请输入你需要拷贝的目录名:")

    # 2 根据该目录名称　创建一个目的目录　－备份
    dest_path = src_path + '-备份'
    os.mkdir(dest_path)

    # 创建一个队列　　－主进程　和　多个完成文件拷贝的子进程之间　进行通信
    queue = multiprocessing.Queue()

    # 3 获取到源目录下使用的文件信息列表 为每个文件复制任务创建一个进程完成
    file_list = os.listdir(src_path)
    for file in file_list:
        # print(file)
        pro = multiprocessing.Process(target=copy_file, args=(src_path, file, dest_path, queue))
        pro.start()

    # 计数　完成拷贝的文件数量
    count = 0
    while True:
        queue.get()
        count += 1
        print("\r 当前进度是%% %f" % (count / len(file_list) * 100), end='')
        time.sleep(0.4)
        if count == len(file_list):
            print("完成拷贝")
            break