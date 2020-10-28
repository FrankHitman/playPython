# encoding=utf-8

import gevent
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore(2)


def worker(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    gevent.sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)


gevent.joinall([gevent.spawn(worker, i) for i in xrange(0, 6)])

# 信号量可以用来限制协程并发的个数。它有两个方法，acquire和release。顾名思义，acquire就是获取信号量，而release就是释放。
# 当所有信号量都已被获取，那剩余的协程就只能等待任一协程释放信号量后才能得以运行：
# 上面的例子中，我们初始化了”BoundedSemaphore”信号量，并将其个数定为2。
# 所以同一个时间，只能有两个worker协程被调度。
# 如果信号量个数为1，那就等同于同步锁。