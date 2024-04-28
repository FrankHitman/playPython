# coding=utf-8
import multiprocessing

def sender(pipe):
    for i in range(5):
        pipe.send("Message {}".format(i))
    pipe.close()

def receiver(pipe):
    while True:
        try:
            msg = pipe.recv()
            print("Received:", msg)
        except EOFError:
            print("Pipe closed, exiting")
            break

if __name__ == "__main__":
    # 创建管道
    sender_pipe, receiver_pipe = multiprocessing.Pipe()

    # 创建发送者和接收者进程
    sender_process = multiprocessing.Process(target=sender, args=(sender_pipe,))
    receiver_process = multiprocessing.Process(target=receiver, args=(receiver_pipe,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("All processes finished")

# output
# (.venv) Franks-Mac:multiple_process frank$ python play_pipe.py
# ('Received:', 'Message 0')
# ('Received:', 'Message 1')
# ('Received:', 'Message 2')
# ('Received:', 'Message 3')
# ('Received:', 'Message 4')
#
# ^CTraceback (most recent call last):
#   File "play_pipe.py", line 30, in <module>
# Process Process-2:
#     receiver_process.join()
#   File "/Users/frank/.pyenv/versions/2.7.18/lib/python2.7/multiprocessing/process.py", line 148, in join
# Traceback (most recent call last):
#   File "/Users/frank/.pyenv/versions/2.7.18/lib/python2.7/multiprocessing/process.py", line 267, in _bootstrap
#     res = self._popen.wait(timeout)
#   File "/Users/frank/.pyenv/versions/2.7.18/lib/python2.7/multiprocessing/forking.py", line 154, in wait
#     self.run()
#   File "/Users/frank/.pyenv/versions/2.7.18/lib/python2.7/multiprocessing/process.py", line 114, in run
#     self._target(*self._args, **self._kwargs)
#   File "play_pipe.py", line 12, in receiver
#     msg = pipe.recv()
# KeyboardInterrupt
#     return self.poll(0)
#   File "/Users/frank/.pyenv/versions/2.7.18/lib/python2.7/multiprocessing/forking.py", line 135, in poll
#     pid, sts = os.waitpid(self.pid, flag)
# KeyboardInterrupt