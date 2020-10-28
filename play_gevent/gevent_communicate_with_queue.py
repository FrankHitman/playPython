# encoding=utf-8

import gevent
from gevent.queue import Queue

products = Queue(3)

def consumer(name):
    while not products.empty():
        print '%s got product %s' % (name, products.get())
        gevent.sleep(0)
    print '%s Quit' %(name)

def producer():
    for i in xrange(1, 10):
        products.put(i)

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'steve'),
    gevent.spawn(consumer, 'john'),
    gevent.spawn(consumer, 'nancy'),
])

# 队列Queue的概念相信大家都知道，我们可以用它的put和get方法来存取队列中的元素。
# gevent的队列对象可以让greenlet协程之间安全的访问。
# 运行下面的程序，你会看到3个消费者会分别消费队列中的产品，且消费过的产品不会被另一个消费者再取到：

# -----output------
# steve got product 1
# john got product 2
# nancy got product 3
# steve got product 4
# john got product 5
# nancy got product 6
# steve got product 7
# john got product 8
# nancy got product 9
# steve Quit
# john Quit
# nancy Quit

# put和get方法都是阻塞式的，它们都有非阻塞的版本：put_nowait和get_nowait。
# 如果调用get方法时队列为空，则抛出”gevent.queue.Empty”异常。