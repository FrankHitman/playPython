# encoding=utf-8
# how main thread catch child thread's exception?

import time
from threading import Thread


class CountDown(Thread):
    def __init__(self):
        super(CountDown, self).__init__()

    def run(self):
        num = 100
        print('slave start')
        for i in range(5, -1, -1):
            print('Num: {0}'.format(num/i))
            time.sleep(1)
        print('slave end')


if __name__ == '__main__':
    print('main start')
    try:
        td = CountDown()
        td.start()
        td.join()
    except Exception as e:
        print('get child thread exception', e) # this line will not be excuted
    print('main end')

# -----output----
# main start
# slave start
# Num: 20.0
# Num: 25.0
# Num: 33.333333333333336
# Num: 50.0
# Num: 100.0
# Exception in thread Thread-1:
# Traceback (most recent call last):
#   File "/usr/local/python3/lib/python3.7/threading.py", line 917, in _bootstrap_inner
#     self.run()
#   File "/home/sdy/play_python/palyPython/play_thread/thread_execept.py", line 14, in run
#     print('Num: {0}'.format(num/i))
# ZeroDivisionError: division by zero
#
# main end

# 可见，子线程产生了异常但并没有被主线程所捕获，因为主线程和子线程分别使用各自的栈，主线程并不能截获子线程调用过程中的异常。
# 在子线程异常退出后，主线程执行了后续代码（此时主线程不知道子线程的退出状态）。reference: https://www.jianshu.com/p/e672152d6753

