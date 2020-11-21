# import time
# def work1():
#     while True:
#         print("in work1")
#         yield
#         time.sleep(1)
#
#
# def work2():
#     while True:
#         print("in work2")
#         yield
#         time.sleep(1)
# if __name__ == "__main__":
#     w1 = work1()
#     w2 = work2()
#     while True:
#         next(w1)
#         next(w2)
# import time
# from greenlet import greenlet
# def work1():
#     while True:
#         print("in work1")
#         g2.switch()
#         time.sleep(1)
# def work2():
#     while True:
#         print("in work2")
#         g1.switch()
#         time.sleep(1)
# g1 = greenlet(work1)
# g2 = greenlet(work2)
# g1.switch()


# from gevent import monkey
# monkey.patch_all()
# import gevent
# import time
# def work1(n):
#     for i in range(n):
#         print("in work %s" % gevent.getcurrent())
#         time.sleep(0.3)
# g1 = gevent.spawn(work1,10)
# g2 = gevent.spawn(work1,10)
# g3 = gevent.spawn(work1,10)
# # g1.join()
# # g2.join()
# gevent.joinall([g1,g2,g3])

# 使用协程完成任务下载
# from gevent import monkey
# monkey.patch_all()
# import gevent
# import urllib.request
# import time
# def down_html(url):
#     print("开始请求"+url)
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     print("获取网页数据成功%s 共计%d字节" % (url,len(data)))
# if __name__=="__main__":
#     begin = time.time()
#     g1 = gevent.spawn(down_html,"http://baidu.com")
#     g2 = gevent.spawn(down_html, "http://itheima.com")
#     g3 = gevent.spawn(down_html,"http://itcast.cn")
#     gevent.joinall([g1,g2,g3])
#     end = time.time()
#     print("共计花费%s" %(end-begin))

# import re
# ret = re.match("[a-z][A-Z]*","m")
# print(ret.group())

import  re
email_list = 








































































































