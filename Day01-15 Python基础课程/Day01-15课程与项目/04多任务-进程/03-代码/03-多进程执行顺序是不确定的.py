import multiprocessing
import time


def worker1(no):
    while True:
        print(no)
        time.sleep(1)


def worker2(no):
    while True:
        print(no)
        time.sleep(1)


if __name__ == '__main__':
    # 多个进程执行顺序不确定
    for i in range(5):
        pro1 = multiprocessing.Process(target=worker1,args=(i,))
        pro1.start()
