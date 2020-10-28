
### 递归锁对象

重入锁是一个可以被同一个线程多次获取的同步基元组件。在内部，它在基元锁的锁定/非锁定状态上附加了 "所属线程" 和 "递归等级" 的概念。在锁定状态下，某些线程拥有锁 ； 在非锁定状态下， 没有线程拥有它。

若要锁定锁，线程调用其 acquire() 方法；一旦线程拥有了锁，方法将返回。若要解锁，线程调用 release() 方法。 acquire()/release() 对可以嵌套；只有最终 release() (最外面一对的 release() ) 将锁解开，才能让其他线程继续处理 acquire() 阻塞。

递归锁也支持 上下文管理协议。

```
class threading.RLock

    此类实现了重入锁对象。重入锁必须由获取它的线程释放。一旦线程获得了重入锁，同一个线程再次获取它将不阻塞；线程必须在每次获取它时释放一次。

    需要注意的是 RLock 其实是一个工厂函数，返回平台支持的具体递归锁类中最有效的版本的实例。

    acquire(blocking=True, timeout=-1)

        可以阻塞或非阻塞地获得锁。

        当无参数调用时： 如果这个线程已经拥有锁，递归级别增加一，并立即返回。否则，如果其他线程拥有该锁，则阻塞至该锁解锁。一旦锁被解锁(不属于任何线程)，则抢夺所有权，设置递归等级为一，并返回。如果多个线程被阻塞，等待锁被解锁，一次只有一个线程能抢到锁的所有权。在这种情况下，没有返回值。

        当调用时参数 blocking 设置为 True ，和没带参数调用一样做同样的事，然后返回 True 。

        当 blocking 参数设置为 false 的情况下调用，不进行阻塞。如果一个无参数的调用已经阻塞，立即返回false；否则，执行和无参数调用一样的操作，并返回true。

        当浮点数 timeout 参数被设置为正值调用时，只要无法获得锁，将最多阻塞 timeout 设定的秒数。 如果锁被获取返回 true，如果超时返回false。

        在 3.2 版更改: 新的 timeout 形参。

    release()

        释放锁，自减递归等级。如果减到零，则将锁重置为非锁定状态(不被任何线程拥有)，并且，如果其他线程正被阻塞着等待锁被解锁，则仅允许其中一个线程继续。如果自减后，递归等级仍然不是零，则锁保持锁定，仍由调用线程拥有。

        只有当前线程拥有锁才能调用这个方法。如果锁被释放后调用这个方法，会引起 RuntimeError 异常。

        没有返回值。
```

```python
class RLock(object):
    # no doc
    def acquire(self, blocking=True): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True) -> bool
        
        Lock the lock.  `blocking` indicates whether we should wait
        for the lock to be available or not.  If `blocking` is False
        and another thread holds the lock, the method will return False
        immediately.  If `blocking` is True and another thread holds
        the lock, the method will wait for the lock to be released,
        take it and then return True.
        (note: the blocking operation is interruptible.)
        
        In all other cases, the method will return True immediately.
        Precisely, if the current thread already holds the lock, its
        internal counter is simply incremented. If nobody holds the lock,
        the lock is taken and its internal counter initialized to 1.
        """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        and must be locked by the same thread that unlocks it; otherwise a
        `RuntimeError` is raised.
        
        Do note that if the lock was acquire()d several times in a row by the
        current thread, release() needs to be called as many times for the lock
        to be available for other threads.
        """
        pass

```