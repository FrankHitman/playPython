# coding=utf-8
import multiprocessing
import os
import time

# 定义一个函数，用于在子进程中执行任务
def worker(name):
    pid = os.getpid()
    print("Worker {} started (pid={})".format(name,pid))
    time.sleep(2)  # 模拟耗时任务
    print("Worker {} finished".format(name))

if __name__ == "__main__":
    # 创建三个子进程，每个子进程执行 worker 函数
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # 等待所有子进程结束
    for p in processes:
        p.join()

    print("All workers finished")

# output
# (.venv) Franks-Mac:multiple_process frank$ python play_multiprocessing.py
# Worker 0 started (pid=32659)
# Worker 1 started (pid=32660)
# Worker 2 started (pid=32661)
# Worker 0 finished
# Worker 1 finished
# Worker 2 finished
# All workers finished