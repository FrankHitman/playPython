# coding: utf-8
# client.py

import grpc
import pi_pb2
import pi_pb2_grpc
import time

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel


# def main():
#     channel = grpc.insecure_channel('localhost:8080')
#     # 使用 stub
#     client = pi_pb2_grpc.PiCalculatorStub(channel)
#     # 调用吧
#     for i in range(1, 1000):
#         value = client.Calc(pi_pb2.PiRequest(n=i)).value
#         # print "pi(%d) =" % i, client.Calc(pi_pb2.PiRequest(n=i)).value


# handle exception in grpc
# -----output----
# [sdy@centos simple]$ python client.py
# pi(0) = StatusCode.INVALID_ARGUMENT request number should be positive
# pi(1) = 2.82842712475
def main():
    # channel = grpc.insecure_channel('localhost:8080')

    chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
                ('grpc.grpc.default_compression_level', CompressionLevel.high)]
    channel = grpc.insecure_channel('localhost:8080', chan_ops)

    client = pi_pb2_grpc.PiCalculatorStub(channel)
    for i in range(2):
        try:
            print "pi(%d) =" % i, client.Calc(pi_pb2.PiRequest(n=i), timeout=5).value
        except grpc.RpcError as e:
            # print e.code(), e.details()
            print e.code(), e.initial_metadata()



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('time cost ', end-start)


# -----output-----
# [sdy@centos play_grpc]$ time python client.py
# ('time cost ', 1.2302160263061523)
#
# real	0m1.364s
# user	0m0.172s
# sys	0m0.251s
