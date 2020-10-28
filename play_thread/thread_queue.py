# encoding=utf-8

# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
# 创建一个被多个线程共享的 Queue 对象，这些线程通过使用put() 和 get() 操作来向队列中添加或者删除元素。

# # maxsize默认为0，不受限
# # 一旦>0，而消息数又达到限制，q.put()也将阻塞
# q = Queue(maxsize=0)
# # 阻塞程序，等待队列消息。
# q.get()
# # 获取消息，设置超时时间
# q.get(timeout=5.0)
# # 发送消息
# q.put()
# # 等待所有的消息都被消费完
# q.join()
# # 以下三个方法，知道就好，代码中不要使用
# # 查询当前队列的消息个数
# q.qsize()
# # 队列消息是否都被消费完，True/False
# q.empty()
# # 检测队列里消息是否已满
# q.full()

from queue import Queue
from threading import Thread
import time


class Student(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            # 阻塞程序，时刻监听老师，接收消息
            msg = self.queue.get()
            # 一旦发现点到自己名字，就赶紧答到
            if msg == self.name:
                print("{}：到！".format(self.name))
                break


class Teacher:
    def __init__(self, queue):
        self.queue = queue

    def call(self, student_name):
        print("老师：{}来了没？".format(student_name))
        # 发送消息，要点谁的名
        self.queue.put(student_name)


queue = Queue()
teacher = Teacher(queue=queue)
s1 = Student(name="小明", queue=queue)
s2 = Student(name="小亮", queue=queue)
s1.start()
s2.start()

print('开始点名~')
teacher.call('小明')
time.sleep(1)
teacher.call('小亮')
# queue.join()

# Python的Queue模块中提供了同步的、线程安全的队列类，
# 包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
# 这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
