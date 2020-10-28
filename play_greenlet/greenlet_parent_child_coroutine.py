# encoding=utf-8

from greenlet import greenlet


def test1():
    print 12
    print greenlet.getcurrent()
    gr2.switch()
    print greenlet.getcurrent()
    print 34
    gr2.switch()


def test2():
    print 56
    print greenlet.getcurrent()


gr1 = greenlet(test1)
gr2 = greenlet(test2, gr1)
gr1.switch()
print 78

# 创建协程对象的方法其实有两个参数”greenlet(run=None, parent=None)”。
# 参数”run”就是其要调用的方法，比如上例中的函数test1()和test2()；
# 参数”parent”定义了该协程对象的父协程，也就是说，greenlet协程之间是可以有父子关系的。
# 如果不设或设为空，则其父协程就是程序默认的”main”主协程。这个”main”协程不需要用户创建，它所对应的方法就是主程序，而所有用户创建的协程都是其子孙。
# 大家可以把greenlet协程集看作一颗树，树的根节点就是”main”，上例中的”gr1″和”gr2″就是其两个字节点。
# 在子协程执行完毕后，会自动返回父协程。

# ----output-----
# 12
# 56
# 34
# 78

# 还有一个重要的点，就是协程退出后，就无法再被执行了。
# 如果上例在函数test1()中，再加一句”gr2.switch()”，运行的结果是一样的。
# 因为第二次调用”gr2.switch()”，什么也不会运行。

# 大家可能会感觉到父子协程之间的关系，就像函数调用一样，一个嵌套一个。
# 的确，其实greenlet协程的实现就是使用了栈，其运行的上下文保存在栈中，”main”主协程处于栈底的位置，而当前运行中的协程就在栈顶。这同函数是一样。
# 此外，在任何时候，你都可以使用”greenlet.getcurrent()”，获取当前运行中的协程对象。
# 比如在函数test2()中执行”greenlet.getcurrent()”，其返回就等于”gr2″。

