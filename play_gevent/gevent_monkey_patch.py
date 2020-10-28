# encoding=utf-8

from gevent import monkey; monkey.patch_socket()
import gevent, time
import socket


urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
print(time.time())

jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)
print(time.time())

print([job.value for job in jobs])
print(time.time())

# 细心的朋友们在运行上面例子时会发现，其实程序运行的时间同不用协程是一样的，是三个网站打开时间的总和。
# 可是理论上协程是非阻塞的，那运行时间应该等于最长的那个网站打开时间呀？
# 其实这是因为Python标准库里的socket是阻塞式的，DNS解析无法并发，包括像urllib库也一样，
# 所以这种情况下用协程完全没意义。那怎么办？
# 一种方法是使用gevent下的socket模块，我们可以通过”from gevent import socket”来导入。
# 不过更常用的方法是使用猴子布丁（Monkey patching）:

#-----output-----
# 1555143931.57
# 1555143931.63
# ['115.239.210.27', '23.100.69.251', '151.101.76.223']
# 1555143931.63
