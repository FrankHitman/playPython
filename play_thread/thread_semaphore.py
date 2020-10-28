# encoding=utf-8
# 信号量通常用于保护数量有限的资源，例如数据库服务器。
# 在资源数量固定的任何情况下，都应该使用有界信号量。
# 在生成任何工作线程前，应该在主线程中初始化信号量。
# https://docs.python.org/zh-cn/3/library/threading.html#threading.Semaphore

# from threading import BoundedSemaphore
# maxconnections = 5
# # ...
# pool_sema = BoundedSemaphore(value=maxconnections)
# with pool_sema:  # 信号量对象也支持 上下文管理协议 。__enter__ = acquire __exit__ = release
#     conn = connectdb()
#     try:
#         pass
#         # ... use connection ...
#     finally:
#         conn.close()

# encoding: UTF-8
import threading
import time

# 计数器初值为2
semaphore = threading.Semaphore(2)


def func():
    # 请求Semaphore，成功后计数器-1；计数器为0时阻塞
    print('%s acquire semaphore...' % threading.currentThread().getName())
    if semaphore.acquire():
        print('%s get semaphore' % threading.currentThread().getName())
        time.sleep(4)

        # 释放Semaphore，计数器+1
        print('%s release semaphore' % threading.currentThread().getName())
        semaphore.release()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t4 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
t4.start()

time.sleep(2)

# 没有获得semaphore的主线程也可以调用release
# 若使用BoundedSemaphore，t4释放semaphore时将抛出异常
print('MainThread release semaphore without acquire')
semaphore.release()

# ----output-----
# Thread-1 acquire semaphore...
# Thread-1 get semaphore
# Thread-2 acquire semaphore...
# Thread-2 get semaphore
# Thread-3 acquire semaphore...
# Thread-4 acquire semaphore...
# MainThread release semaphore without acquire
# Thread-3 get semaphore
# Thread-1 release semaphore
# Thread-4 get semaphore
# Thread-2 release semaphore
# Thread-3 release semaphore
# Thread-4 release semaphore


# Semaphore（信号量），同步指令。Semaphore管理一个内置的计数器，每当调用acquire()时-1，调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。
# 基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。
# BoundedSemaphore 与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，如果超过了将抛出一个异常。
# https://superxiaoxiong.github.io/2016/07/27/python-threading/
