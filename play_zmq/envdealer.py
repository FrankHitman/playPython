"""

   Pubsub envelope publisher

   Author: Guillaume Aubert (gaubert) <guillaume(dot)aubert(at)gmail(dot)com>

"""
import time
import zmq

def main():
    """main method"""

    # Prepare our context and publisher
    context   = zmq.Context()
    publisher = context.socket(zmq.DEALER)
    publisher.identity='dealer1'
    publisher.connect("tcp://127.0.0.1:5563")

    while True:
        # Write two messages, each with an envelope and content
        publisher.send("We don't want to see this")
        # publisher.send_multipart([b"B", b"We would like to see this"])
        time.sleep(1)
        msg = publisher.recv()
        print('rec: '+ msg)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()


if __name__ == "__main__":
    main()