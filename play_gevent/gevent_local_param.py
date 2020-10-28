# encoding=utf-8

import gevent
from gevent.local import local

data = local()


def f1():
    data.x = 1
    print data.x


def f2():
    try:
        print data.x
    except AttributeError:
        print 'x is not visible'


gevent.joinall([
    gevent.spawn(f1),
    gevent.spawn(f2)
])

# 通过将变量存放在local对象中，即可将其的作用域限制在当前协程内，当其他协程要访问该变量时，就会抛出异常。
# 不同协程间可以有重名的本地变量，而且互相不影响。
# 因为协程本地变量的实现，就是将其存放在以的”greenlet.getcurrent()”的返回为键值的私有的命名空间内。