
### 在 with 语句中使用锁、条件和信号量
这个模块提供的带有 acquire() 和 release() 方法的对象，可以被用作 with 语句的上下文管理器。
当进入语句块时 acquire() 方法会被调用，退出语句块时 release() 会被调用。因此，以下片段:
```python
with some_lock:
    # do something...
```
相当于:
```python
some_lock.acquire()
try:
# do something...
finally:
    some_lock.release()
    
```

现在 Lock 、 RLock 、 Condition 、 Semaphore 和 BoundedSemaphore 对象可以用作 with 语句的上下文管理器。

- [reference](https://docs.python.org/zh-cn/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement)

Detail refer to the source code, They are all implement __enter__ and __exit__ function.
such as Semaphore.  
```python

class Semaphore:
    """This class implements semaphore objects.

    Semaphores manage a counter representing the number of release() calls minus
    the number of acquire() calls, plus an initial value. The acquire() method
    blocks if necessary until it can return without making the counter
    negative. If not given, value defaults to 1.

    """

    # After Tim Peters' semaphore class, but not quite the same (no maximum)

    def __init__(self, value=1):
        if value < 0:
            raise ValueError("semaphore initial value must be >= 0")
        self._cond = Condition(Lock())
        self._value = value

    def acquire(self, blocking=True, timeout=None):
        """Acquire a semaphore, decrementing the internal counter by one.

        When invoked without arguments: if the internal counter is larger than
        zero on entry, decrement it by one and return immediately. If it is zero
        on entry, block, waiting until some other thread has called release() to
        make it larger than zero. This is done with proper interlocking so that
        if multiple acquire() calls are blocked, release() will wake exactly one
        of them up. The implementation may pick one at random, so the order in
        which blocked threads are awakened should not be relied on. There is no
        return value in this case.

        When invoked with blocking set to true, do the same thing as when called
        without arguments, and return true.

        When invoked with blocking set to false, do not block. If a call without
        an argument would block, return false immediately; otherwise, do the
        same thing as when called without arguments, and return true.

        When invoked with a timeout other than None, it will block for at
        most timeout seconds.  If acquire does not complete successfully in
        that interval, return false.  Return true otherwise.

        """
        if not blocking and timeout is not None:
            raise ValueError("can't specify timeout for non-blocking acquire")
        rc = False
        endtime = None
        with self._cond:
            while self._value == 0:
                if not blocking:
                    break
                if timeout is not None:
                    if endtime is None:
                        endtime = _time() + timeout
                    else:
                        timeout = endtime - _time()
                        if timeout <= 0:
                            break
                self._cond.wait(timeout)
            else:
                self._value -= 1
                rc = True
        return rc

    __enter__ = acquire

    def release(self):
        """Release a semaphore, incrementing the internal counter by one.

        When the counter is zero on entry and another thread is waiting for it
        to become larger than zero again, wake up that thread.

        """
        with self._cond:
            self._value += 1
            self._cond.notify()

    def __exit__(self, t, v, tb):
        self.release()


```