# coding=utf-8
import multiprocessing
import time

def producer(queue):
    for i in range(5):
        print("Producing item {}".format(i))
        time.sleep(1)
        queue.put(i)  # 将数据放入队列
    queue.put(None)  # 表示生产结束

def consumer(queue):
    while True:
        item = queue.get()  # 从队列中获取数据
        if item is None:
            print("Consumer received None, exiting")
            break
        print("Consuming item {}".format(item))
        time.sleep(2)

if __name__ == "__main__":
    queue = multiprocessing.Queue()  # 创建一个队列

    # 创建生产者和消费者进程
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    # 是阻塞的等待，timeout 是 None
    # res = self._popen.wait(timeout)
    # self.poll(0)
    # pid, sts = os.waitpid(self.pid, 0) 0代表是阻塞的
    # os.WNOHANG 代表非阻塞，直接返回
    producer_process.join()
    consumer_process.join()

    print("All processes finished")

# output
# (.venv) Franks-Mac:multiple_process frank$ python play_queue.py
# Producing item 0
# Producing item 1
# Consuming item 0
# Producing item 2
# Producing item 3
# Consuming item 1
# Producing item 4
# Consuming item 2
# Consuming item 3
# Consuming item 4
# Consumer received None, exiting
# All processes finished