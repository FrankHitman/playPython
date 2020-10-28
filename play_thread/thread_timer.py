# encoding=utf-8

# 这个类表示一个动作应该在一个特定的时间之后运行 — 也就是一个计时器。Timer是Thread的子类， 因此也可以使用函数创建自定义线程
# Timers通过调用它们的start()方法作为线程启动。timer可以通过调用cancel()方法（在它的动作开始之前）停止。timer在执行它的动作之前等待的时间间隔可能与用户指定的时间间隔不完全相同。

from threading import Timer
from threading import activeCount

def hello():
    print("hello, world")


t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed

# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
