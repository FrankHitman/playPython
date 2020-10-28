# encoding=utf-8


# 锁被占用时使用(否则将会报RuntimeError异常)
# Condition和Event 是类似的，并没有多大区别。同样，Condition也只需要掌握几个函数即可。
# cond = threading.Condition()
# # 类似lock.acquire()
# cond.acquire()
# # 类似lock.release()
# cond.release()
# # 锁被占用时使用(否则将会报RuntimeError异常), wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。
# # 当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。reference: https://superxiaoxiong.github.io/2016/07/27/python-threading/
# cond.wait()
# # 唤醒一个挂起的线程（如果存在挂起的线程）。注意：notify()方法不会释放所占用的琐。
# cond.notify()

import threading, time
from threading import Lock, RLock


class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)  # 确保先运行Hider中的方法, otherwise seeker and hider will be dead locking
        self.cond.acquire()

        print(self.name + ': 我已经把眼睛蒙上了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我找到你了哦 ~_~')
        self.cond.notify()

        self.cond.release()
        print(self.name + ': 我赢了')


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ': 我已经藏好了，你快来找我吧')
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print(self.name + ': 被你找到了，哎~~~')


cond = threading.Condition(Lock())  # default is RLock
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()

# 通过cond来通信，阻塞自己，并使对方执行。从而，达到有顺序的执行。
# ----output----
# seeker: 我已经把眼睛蒙上了
# hider: 我已经藏好了，你快来找我吧
# seeker: 我找到你了哦 ~_~
# seeker: 我赢了
# hider: 被你找到了，哎~~~

# Condition被称为条件变量，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。
# 线程首先acquire一个条件变量，然后判断一些条件。如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，
# 其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。
# 可以认为Condition对象维护了一个锁（Lock/RLock)和一个waiting池。线程通过acquire获得Condition对象，
# 当调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。
# 当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁。
# Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock。

# Condition use RLock.acquire and RLock.release. Source code as below
# class Condition:
#     """Class that implements a condition variable.
#
#     A condition variable allows one or more threads to wait until they are
#     notified by another thread.
#
#     If the lock argument is given and not None, it must be a Lock or RLock
#     object, and it is used as the underlying lock. Otherwise, a new RLock object
#     is created and used as the underlying lock.
#
#     """
#
#     def __init__(self, lock=None):
#         if lock is None:
#             lock = RLock()
#         self._lock = lock
#         # Export the lock's acquire() and release() methods
#         self.acquire = lock.acquire
#         self.release = lock.release
#         # If the lock defines _release_save() and/or _acquire_restore(),
#         # these override the default implementations (which just call
#         # release() and acquire() on the lock).  Ditto for _is_owned().
#         try:
#             self._release_save = lock._release_save
#         except AttributeError:
#             pass
#         try:
#             self._acquire_restore = lock._acquire_restore
#         except AttributeError:
#             pass
#         try:
#             self._is_owned = lock._is_owned
#         except AttributeError:
#             pass
#         self._waiters = _deque()
#
#     def __enter__(self):
#         return self._lock.__enter__()
#
#     def __exit__(self, *args):
#         return self._lock.__exit__(*args)
#
#     def __repr__(self):
#         return "<Condition(%s, %d)>" % (self._lock, len(self._waiters))
#
#     def _release_save(self):
#         self._lock.release()           # No state to save
#
#     def _acquire_restore(self, x):
#         self._lock.acquire()           # Ignore saved state
#
#     def _is_owned(self):
#         # Return True if lock is owned by current_thread.
#         # This method is called only if _lock doesn't have _is_owned().
#         if self._lock.acquire(0):
#             self._lock.release()
#             return False
#         else:
#             return True
#
#     def wait(self, timeout=None):
#         """Wait until notified or until a timeout occurs.
#
#         If the calling thread has not acquired the lock when this method is
#         called, a RuntimeError is raised.
#
#         This method releases the underlying lock, and then blocks until it is
#         awakened by a notify() or notify_all() call for the same condition
#         variable in another thread, or until the optional timeout occurs. Once
#         awakened or timed out, it re-acquires the lock and returns.
#
#         When the timeout argument is present and not None, it should be a
#         floating point number specifying a timeout for the operation in seconds
#         (or fractions thereof).
#
#         When the underlying lock is an RLock, it is not released using its
#         release() method, since this may not actually unlock the lock when it
#         was acquired multiple times recursively. Instead, an internal interface
#         of the RLock class is used, which really unlocks it even when it has
#         been recursively acquired several times. Another internal interface is
#         then used to restore the recursion level when the lock is reacquired.
#
#         """
#         if not self._is_owned():
#             raise RuntimeError("cannot wait on un-acquired lock")
#         waiter = _allocate_lock()
#         waiter.acquire()
#         self._waiters.append(waiter)
#         saved_state = self._release_save()
#         gotit = False
#         try:    # restore state no matter what (e.g., KeyboardInterrupt)
#             if timeout is None:
#                 waiter.acquire()
#                 gotit = True
#             else:
#                 if timeout > 0:
#                     gotit = waiter.acquire(True, timeout)
#                 else:
#                     gotit = waiter.acquire(False)
#             return gotit
#         finally:
#             self._acquire_restore(saved_state)
#             if not gotit:
#                 try:
#                     self._waiters.remove(waiter)
#                 except ValueError:
#                     pass
#
#     def wait_for(self, predicate, timeout=None):
#         """Wait until a condition evaluates to True.
#
#         predicate should be a callable which result will be interpreted as a
#         boolean value.  A timeout may be provided giving the maximum time to
#         wait.
#
#         """
#         endtime = None
#         waittime = timeout
#         result = predicate()
#         while not result:
#             if waittime is not None:
#                 if endtime is None:
#                     endtime = _time() + waittime
#                 else:
#                     waittime = endtime - _time()
#                     if waittime <= 0:
#                         break
#             self.wait(waittime)
#             result = predicate()
#         return result
#
#     def notify(self, n=1):
#         """Wake up one or more threads waiting on this condition, if any.
#
#         If the calling thread has not acquired the lock when this method is
#         called, a RuntimeError is raised.
#
#         This method wakes up at most n of the threads waiting for the condition
#         variable; it is a no-op if no threads are waiting.
#
#         """
#         if not self._is_owned():
#             raise RuntimeError("cannot notify on un-acquired lock")
#         all_waiters = self._waiters
#         waiters_to_notify = _deque(_islice(all_waiters, n))
#         if not waiters_to_notify:
#             return
#         for waiter in waiters_to_notify:
#             waiter.release()
#             try:
#                 all_waiters.remove(waiter)
#             except ValueError:
#                 pass
#
#     def notify_all(self):
#         """Wake up all threads waiting on this condition.
#
#         If the calling thread has not acquired the lock when this method
#         is called, a RuntimeError is raised.
#
#         """
#         self.notify(len(self._waiters))
#
#     notifyAll = notify_all
