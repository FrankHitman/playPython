# coding=utf-8
import gevent
from gevent import monkey

# 打补丁，使标准库中的阻塞 I/O 函数变为非阻塞的异步调用
monkey.patch_all()

def task1():
    for i in range(5):
        print("Task 1 - Step", i)
        gevent.sleep(1)  # 模拟耗时操作
    print("Task 1 - Finished")

def task2():
    for i in range(5):
        print("Task 2 - Step", i)
        gevent.sleep(0.5)  # 模拟耗时操作
    print("Task 2 - Finished")

if __name__ == "__main__":
    # 创建两个协程任务
    greenlet1 = gevent.spawn(task1)
    greenlet2 = gevent.spawn(task2)

    # 等待所有协程任务完成
    gevent.joinall([greenlet1, greenlet2])

# output
# (.venv) Franks-Mac:play_gevent frank$ python async_task.py
# ('Task 1 - Step', 0)
# ('Task 2 - Step', 0)
# ('Task 2 - Step', 1)
# ('Task 1 - Step', 1)
# ('Task 2 - Step', 2)
# ('Task 2 - Step', 3)
# ('Task 1 - Step', 2)
# ('Task 2 - Step', 4)
# Task 2 - Finished
# ('Task 1 - Step', 3)
# ('Task 1 - Step', 4)
# Task 1 - Finished