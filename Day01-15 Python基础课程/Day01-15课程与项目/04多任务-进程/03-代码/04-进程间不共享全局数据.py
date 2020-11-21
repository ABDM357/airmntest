import multiprocessing
import time

g_number = 0

def worker1(no):
    print(g_number)
    global g_number
    g_number += 99
    while True:
        time.sleep(1)
        print("worker1 获取到的%d" % g_number)


def worker2(no):
    while True:
        time.sleep(1)
        print("worker２ 获取到的%d" % g_number)


if __name__ == '__main__':
    # 多个进程内部不共享全局数据　　－－－－> 每个进程是独立的数据空间
    # 在主进程创建子进程的时候　　会将全局数据给子进程拷贝一份　
    # 在子进程中修改全局数据不影响其他进程的全局数据
    pro1 = multiprocessing.Process(target=worker1,args=(0,))
    pro1.start()

    pro2 = multiprocessing.Process(target=worker2,args=(1,))
    pro2.start()

