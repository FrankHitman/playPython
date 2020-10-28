# coding:utf8
import gevent
from gevent.event import Event

evt = Event()


def setter():
    print 'Wait for me'
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print "Ok, I'm done"
    print evt.ready()
    evt.set()  # 唤醒
    print evt.ready()


def waiter():
    print "I'll wait for you"
    evt.wait()  # 等待
    print 'Finish waiting'


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter)
])

# greenlet协程间的异步通讯可以使用事件（Event）对象。
# 该对象的”wait()”方法可以阻塞当前协程，而”set()”方法可以唤醒之前阻塞的协程。
# 在下面的例子中，5个waiter协程都会等待事件evt，当setter协程在3秒后设置evt事件，所有的waiter协程即被唤醒。
#-----output------
# Wait for me
# I'll wait for you
# I'll wait for you
# I'll wait for you
# I'll wait for you
# I'll wait for you
# Ok, I'm done
# False
# True
# Finish waiting
# Finish waiting
# Finish waiting
# Finish waiting
# Finish waiting