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
    pro = multiprocessing.Process(target=proc_func, args=(100,), name='SSS',kwargs={'age':18})

    # PID process identify
    # os.getpid() 获取当前进程的ＰＩＤ
    # os.getppid() parent process identify 获取当前进程的父进程的PID
    # 启动子进程的创建和执行

    # 如果子进程还没有创建　　则获取不到PID
    # print(pro.pid)

    pro.start()

    # 获取进程对象标识的　进程的名称
    print(pro.name)
    # os.getpid()
    print(pro.pid)
    print(pro.is_alive())

    # terminate()作用是告诉操作系统 让子进程退出 -----> 产生了时间差
    # pro.terminate()
    # time.sleep(0.1)
    pro.join()
    print(pro.is_alive())
