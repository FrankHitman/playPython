# coding: utf-8
# server.py
import math
import grpc
import time
import random
from concurrent import futures

import pi_pb2
import pi_pb2_grpc


class PiCalculatorServicer(pi_pb2_grpc.PiCalculatorServicer):

    def Calc(self, request_iterator, ctx):
        # request 是一个迭代器参数，对应的是一个 stream 请求
        for request in request_iterator:
            # 50% 的概率会有响应
            if random.randint(0, 1) == 1:
                continue
            s = 0.0
            for i in range(request.n):
                s += 1.0/(2*i+1)/(2*i+1)
            # 响应是一个生成器，一个响应对应对应一个请求
            yield pi_pb2.PiResponse(n=i, value=math.sqrt(8*s))


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = PiCalculatorServicer()
    pi_pb2_grpc.add_PiCalculatorServicer_to_server(servicer, server)
    server.add_insecure_port('localhost:8080')
    server.start()
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()