import time
import threading

# Python提供了非常简单的通信机制 Threading.Event，通用的条件变量。多个线程可以等待某个事件的发生，在事件发生后，所有的线程都会被激活。
#
# 关于Event的使用也超级简单，就三个函数
# event = threading.Event()
# # 重置event，使得所有该event事件都处于待命状态
# event.clear()
# # 等待接收event的指令，决定是否阻塞程序执行
# event.wait()
# # 发送event指令，使所有设置该event事件的线程执行
# event.set()
# refer https://www.cnblogs.com/wongbingming/p/9035579.html

# Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。
# Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print('Thread: {} start at {}'.format(self.name, time.ctime(time.time())))
        # 等待event.set()后，才能往下执行
        self.event.wait()
        print('Thread: {} finish at {}'.format(self.name, time.ctime(time.time())))


threads = []
event = threading.Event()

# 定义五个线程
[threads.append(MyThread(str(i), event)) for i in range(1,5)]

# 重置event，使得event.wait()起到阻塞作用
event.clear()

# 启动所有线程
[t.start() for t in threads]

print('等待5s...')
time.sleep(5)

print('唤醒所有线程...')
event.set()

# -----output-----
# Thread: 1 start at Fri Apr 19 21:16:36 2019
# Thread: 2 start at Fri Apr 19 21:16:36 2019
# Thread: 3 start at Fri Apr 19 21:16:36 2019
# Thread: 4 start at Fri Apr 19 21:16:36 2019
# 等待5s...
# 唤醒所有线程...
# Thread: 1 finish at Fri Apr 19 21:16:41 2019
# Thread: 2 finish at Fri Apr 19 21:16:41 2019
# Thread: 3 finish at Fri Apr 19 21:16:41 2019
# Thread: 4 finish at Fri Apr 19 21:16:41 2019


# Event source code
# class Event:
#     """Class implementing event objects.
#
#     Events manage a flag that can be set to true with the set() method and reset
#     to false with the clear() method. The wait() method blocks until the flag is
#     true.  The flag is initially false.
#
#     """
#
#     # After Tim Peters' event class (without is_posted())
#
#     def __init__(self):
#         self._cond = Condition(Lock())
#         self._flag = False
#
#     def _reset_internal_locks(self):
#         # private!  called by Thread._reset_internal_locks by _after_fork()
#         self._cond.__init__(Lock())
#
#     def is_set(self):
#         """Return true if and only if the internal flag is true."""
#         return self._flag
#
#     isSet = is_set
#
#     def set(self):
#         """Set the internal flag to true.
#
#         All threads waiting for it to become true are awakened. Threads
#         that call wait() once the flag is true will not block at all.
#
#         """
#         with self._cond:
#             self._flag = True
#             self._cond.notify_all()
#
#     def clear(self):
#         """Reset the internal flag to false.
#
#         Subsequently, threads calling wait() will block until set() is called to
#         set the internal flag to true again.
#
#         """
#         with self._cond:
#             self._flag = False
#
#     def wait(self, timeout=None):
#         """Block until the internal flag is true.
#
#         If the internal flag is true on entry, return immediately. Otherwise,
#         block until another thread calls set() to set the flag to true, or until
#         the optional timeout occurs.
#
#         When the timeout argument is present and not None, it should be a
#         floating point number specifying a timeout for the operation in seconds
#         (or fractions thereof).
#
#         This method returns the internal flag on exit, so it will always return
#         True except if a timeout is given and the operation times out.
#
#         """
#         with self._cond:
#             signaled = self._flag
#             if not signaled:
#                 signaled = self._cond.wait(timeout)
#             return signaled
