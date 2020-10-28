# encoding=utf-8
from threading import Thread
import time
import traceback
import sys

class CountDown(Thread):
    def __init__(self):
        super(CountDown, self).__init__()
        self.exitcode = 0
        self.exception = None
        self.exc_traceback = ''

    def run(self):
        try:
            self._run()
        except Exception as e:
            self.exitcode = 1
            self.exception = e
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))

    def _run(self):
        num = 100
        print('slave start')
        for i in range(5, -1, -1):
            print('Num: {0}'.format(num/i))
            time.sleep(1)
        print('slave end')


if __name__ == '__main__':
    print('main start')
    td = CountDown()
    td.start()
    td.join()
    if td.exitcode != 0:
        print('Exception in ' + td.getName() + ' (catch by main)')
        print(td.exc_traceback)
    print('main end')

# -----output-----
# main start
# slave start
# Num: 20.0
# Num: 25.0
# Num: 33.333333333333336
# Num: 50.0
# Num: 100.0
# Exception in Thread-1 (catch by main)
# Traceback (most recent call last):
#   File "/home/sdy/play_python/palyPython/play_thread/thread_catch_except.py", line 16, in run
#     self._run()
#   File "/home/sdy/play_python/palyPython/play_thread/thread_catch_except.py", line 26, in _run
#     print('Num: {0}'.format(num/i))
# ZeroDivisionError: division by zero
#
# main end

# 由于子线程运行结束后，其内存并没有被回收，因此可以继续使用该实例获得其成员变量。
# 基于这一点，我们可以通过添加模拟线程退出信息的成员变量来记录子线程退出状态。
# 可通过sys和traceback两个库实现这一点（完整Demo）。通过检查子线程exitcode，主线程可以知道其退出状态，然后做相应的处理。
# https://www.jianshu.com/p/e672152d6753
