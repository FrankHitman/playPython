# Multi-thread Programming
简述 [reference](https://superxiaoxiong.github.io/2016/07/27/python-threading/)

python代码执行由python虚拟机(解释器主循环)来控制，python虚拟机使用全局解释器锁(GIL)来控制，锁保证同一时刻只有一个线程在运行，对于 I/O密集型程序有很大优势。

python中有Thread和Threading等模块支持线程，Thread模块比较偏底层，本文对于Threading模块进行讲解。
### Threading模块对象
python的threading模块是对thread进行了二次封装，提供了更加便捷的API。经常和Queue结合使用,Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步

- Thread        表示一个线程的执行对象
- Lock          锁原语
- Rlock         可重入锁，使单线程可以再次获得已经获得的锁
- Condition     条件变量，让一个线程等待
- Event         通用条件变量，激活和让多个线程等待
- Semaphore     为等待锁的线程提供一个等待室的结构

### Thread类
Threading的Thread类是主要的运行对象
```
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
应该始终以关键字参数调用该构造函数。参数有：

    group应该为None；被保留用于未来实现了ThreadGroup类时的扩展。
    target是将被run()方法调用的可调用对象。默认为None，表示不调用任何东西。
    name是线程的名字。默认情况下，以“Thread-N”的形式构造一个唯一的名字，N是一个小的十进制整数。
    args是给调用目标的参数元组。默认为()。
    kwargs是给调用目标的关键字参数的一个字典。默认为{}。

如果子类覆盖该构造函数，它必须保证在对线程做任何事之前调用基类的构造函数(Thread.__init__())
```

### Thread类运行函数

- start()             开始线程的执行,在相同的线程对象上调用该方法多次将引发一个RuntimeError
- run()               定义线程的功能的函数(一般子类重写)
- join(timeout=None)  程序挂起，直到线程结束，time不为None，表示最多挂起时间
- getName()           返回线程的名字
- setName(name)       设置线程的名字
- isAlive()           布尔标志，表示某个线程是否在运行
- isDaemon()          返回线程的daemon标志
- setDaemon(daemonic) 设置Daemon位为daemonic，在start运行前调用
- name                线程表示, 没有任何语义
- ident               线程的ID，如果线程还未启动则为None。它是一个非零的整数
```
about daemon
    if set child thread daemon=false, then main thread will waite the child thread finished
    if set child thread daemon=true, then main thread will not waite the child thread finished
    if set child thread daemon=true, but use thread.join() in main thread, then main thread will waite the child thread finished
```
### 从Thread派生
从Thread派生出一个子类，创建这个子类的实例

这是目前比较常用的方法，创建一个新的class，把线程执行的代码放到class里，只覆盖该类的__init__()和run()方法





