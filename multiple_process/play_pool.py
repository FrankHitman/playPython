# coding=utf-8
import multiprocessing
import time

def square(x):
    return x * x

if __name__ == "__main__":
    # 创建一个进程池
    with multiprocessing.Pool(processes=3) as pool:
        # 使用 map 函数将任务分发给进程池
        result = pool.map(square, range(10))
        print("Result:", result)
