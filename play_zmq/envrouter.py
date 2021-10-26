#encoding=utf-8
"""

   Pubsub envelope subscriber

   Author: Guillaume Aubert (gaubert) <guillaume(dot)aubert(at)gmail(dot)com>

"""
import zmq


def main():
    """ main method """

    # Prepare our context and publisher
    context = zmq.Context()
    subscriber = context.socket(zmq.ROUTER)
    subscriber.bind("tcp://*:5563")
    # subscriber.setsockopt(zmq.SUBSCRIBE, b"B")

    while True:
        # Read envelope with address
        origin, message = subscriber.recv_multipart()
        print(origin, message)

        # 发送后dealer收不到消息，会block住，可能因为是一问一答的限制
        # subscriber.send('hello' + str(origin))

        # 会给来源发送回复，来源可以自定义identity属性
        subscriber.send_multipart([origin, 'hello' + str(origin)])
        # [address, contents] = subscriber.recv_multipart()
        # print("[%s] %s" % (address, contents))

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()


if __name__ == "__main__":
    main()
