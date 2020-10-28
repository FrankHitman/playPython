### Lock对象

锁是同步原语，并不归某个特定线程所有。最底层的同步原语。

锁有两种状态locked或者unlocked，创建时处于unlocked状态。

锁有两个基本方法acquire()和release()。
-    当状态是unlocked时，acquire()改变该状态为locked并立即返回。
-    当状态是locked时，acquire()将阻塞直至在另外一个线程中调用release()来将它变为unlocked，然后acquire()调用将它重置为locked并返回
-    release()方法应该只在locked状态下调用；它改变状态为unlocked并立即返回。
-    如果尝试释放一个unlocked的锁，将引发一个RuntimeError。

#### 加锁 Lock.acquire([blocking])
-    blocking参数设置为True（默认值).将阻塞直至锁变成unlock状态，直到他的状态为locked并返回True
-    如果设置为False，当阻塞存在是直接返回False，没有阻塞时locked并返回True

#### 释放一把锁 Lock.release()
- 没有返回值

#### 使用实例
```
>>> from threading import Lock
>>> lock = threading.Lock()
>>> lock.acquire()
True
>>> lock.acquire()

^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>> lock.acquire(False)
False
>>>
>>> lock.release()
>>> lock.release()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: release unlocked lock
>>>
```


