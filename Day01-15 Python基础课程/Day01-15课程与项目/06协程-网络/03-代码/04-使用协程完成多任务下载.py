from gevent import monkey
# monkey.patch_all()
import gevent
import time
import urllib.request

def down_html(url):
    # url就是网址
    print("开始请求" + url)
    # 向远处服务器发起请求  得到一个结果对象 recv
    response = urllib.request.urlopen(url)
    # 从结果对象中获取到数据      # 写入文件
    data = response.read()

    print("获取网页数据成功 %s 共计%d字节" %(url, len(data)))

if __name__ == '__main__':
    begin = time.time()

    g1 = gevent.spawn(down_html,'http://baidu.com')
    g2 = gevent.spawn(down_html,'http://itheima.com')
    g3 = gevent.spawn(down_html,'http://itcast.cn')

    gevent.joinall([g1,g2,g3])
    end = time.time()

    print("总共花费 %fs" % (end-begin))