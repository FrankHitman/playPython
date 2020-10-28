# encoding=utf-8

from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()

# 12
# 56
# 34

# 使用switch()方法切换协程，也比”yield”, “next/send”组合要直观的多。
# 上例中，我们也可以看出，greenlet协程的运行，其本质是串行的，所以它不是真正意义上的并发，因此也无法发挥CPU多核的优势，
# 不过，这个可以通过协程+进程组合的方式来解决，本文就不展开了。
# 另外要注意的是，在没有进行显式切换时，部分代码是无法被执行到的，比如上例中的”print 78″。