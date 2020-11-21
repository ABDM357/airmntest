import multiprocessing
import time

"""主进程往队列中放入屏幕上输入的数据　　子进程从队列中取出数据并且打印出来"""


def proc_func(queue):
    while True:
        if queue.empty():
            print("队列是空的　我稍后来取一次")
            time.sleep(2)
        else:
            data = queue.get()
            print("从队列中取出数据%s" % data)
            time.sleep(2)

if __name__ == '__main__':
    # １　创建一个队列 参数表示队列的最大长度
    queue = multiprocessing.Queue(3)

    # 2　创建一个子进程
    pro = multiprocessing.Process(target=proc_func, args=(queue,))
    pro.start()

    # 3 录入数据　放入队列
    while True:
        if queue.full():
            print("队列已满")
            time.sleep(1)
        else:
            data = input("请输入:")
            queue.put(data)

        print("当前队列数据条数是%s" % queue.qsize())
        """如何创建队列　放数据　取数据"""