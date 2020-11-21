import time
import multiprocessing
import os


def proc_func(number,age):
    print(age)
    print("这是子进程%d PID:%d 父进程的PID:%d" % (number,os.getpid(),os.getppid()))
    for i in range(3):
        print("这是子进程")
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个子进程　
    # 创建一个进程的执行计划 target指定子进程执行的函数代码 args指定函数代码所需的参数
    pro = multiprocessing.Process(target=proc_func, args=(100,), kwargs={'age':18})

    # PID process identify
    # os.getpid() 获取当前进程的ＰＩＤ
    # os.getppid() parent process identify 获取当前进程的父进程的PID
    # 启动子进程的创建和执行
    pro.start()

    # 用来判断子进程是否存活  存活返回True 退出了返回False
    print(pro.is_alive())

    # 用来阻塞等待子进程结束 然后才会继续往下执行 如果有参数 则表示阻塞等待的超时时间
    pro.join(1)
    print("join1 ")
    print(pro.is_alive())
    pro.join()
    print(pro.is_alive())
    # while True:
    #     print("这是主进程 PID:%d" % os.getpid())
    #     time.sleep(1)
    #     """如果创建子进程 怎么获取当前进程PID 当前进程的父进程的PID(PPID)"""