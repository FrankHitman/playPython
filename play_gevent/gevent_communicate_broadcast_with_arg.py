# encoding=utf-8
import gevent
from gevent.event import AsyncResult

aevt = AsyncResult()


def setter():
    print 'Wait for me'
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print "Ok, I'm done"
    aevt.set('Hello!')  # 唤醒，并传递消息


def waiter():
    print("I'll wait for you")
    message = aevt.get()  # 等待，并在唤醒时获取消息
    print 'Got wake up message: %s' % message


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter)
])

# 除了Event事件外，gevent还提供了AsyncResult事件，它可以在唤醒时传递消息。
# 让我们将上例中的setter和waiter作如下改动:

#-----output-----
# Wait for me
# I'll wait for you
# I'll wait for you
# I'll wait for you
# I'll wait for you
# I'll wait for you
# Ok, I'm done
# Got wake up message: Hello!
# Got wake up message: Hello!
# Got wake up message: Hello!
# Got wake up message: Hello!
# Got wake up message: Hello!