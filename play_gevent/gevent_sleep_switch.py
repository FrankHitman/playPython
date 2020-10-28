# coding=utf-8
import gevent


def test1():
    print 12
    gevent.sleep(0)
    print 34


def test2():
    print 56
    gevent.sleep(0)
    print 78


gevent.joinall([
    gevent.spawn(test1),
    gevent.spawn(test2),
])

# 解释下，”gevent.spawn()”方法会创建一个新的greenlet协程对象，并运行它。
# ”gevent.joinall()”方法会等待所有传入的greenlet协程运行结束后再退出，
# 这个方法可以接受一个”timeout”参数来设置超时时间，单位是秒。
# 运行上面的程序，执行顺序如下：
# 12
# 56
# 34
# 78