# encoding=utf-8

import sys
import gc
import time


class ClassA():
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))

    def __del__(self):
        print('object del,id:%s' % str(hex(id(self))))


def f1():
    for i in range(1):
        c1 = ClassA()
        # del c1
        # sys.getrefcount(a)可以查看a对象的引用计数，但是比正常计数大1，因为调用函数的时候传入a，这会让a的引用计数+1
        print(sys.getrefcount(c1))
        c2 = ClassA()
        print(sys.getrefcount(c2))

        del c2
        print(sys.getrefcount(c2))


def f2():
    # 循环引用导致内存泄露 circle reference
    for i in range(1):
        c1 = ClassA()
        c2 = ClassA()
        print(sys.getrefcount(c1))
        print(sys.getrefcount(c2))
        c1.t = c2
        c2.t = c1

        print(sys.getrefcount(c1))
        print(sys.getrefcount(c2))

        del c1
        del c2

        print(sys.getrefcount(c1))
        print(sys.getrefcount(c2))


def f3():
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print(gc.get_count())
    del c1
    print(gc.get_count())
    del c2
    print(gc.garbage)
    print(gc.collect())
    print(gc.garbage)
    time.sleep(10)


if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK)
    f3()
