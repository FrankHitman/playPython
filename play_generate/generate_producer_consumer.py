# encoding=utf-8

def consumer():
    last = ''
    while True:
        receival = yield last
        if receival is not None:
            print('Consume %s' % receival)
            last = receival


def producer(gen, n):
    gen.next()
    x = 0
    while x < n:
        print("then")
        x += 1
        print('Produce %s' % x)
        last = gen.send(x * 2)
        print("last is", last)

    gen.close()


gen = consumer()
producer(gen, 5)

# 执行下例子，你会看到控制台交替打印出生产和消费的结果。
# 消费者consumer()函数是一个生成器函数，每次执行到yield时即挂起，并返回上一次的结果给生产者。
# 生产者producer()接收到生成器的返回，并生成一个新的值，通过send()方法发送给消费者。
# 至此，我们成功实现了一个（伪）并发。
# then
# Produce 1
# Consume 2
# last is 2
# then
# Produce 2
# Consume 4
# last is 4
# then
# Produce 3
# Consume 6
# last is 6
# then
# Produce 4
# Consume 8
# last is 8
# then
# Produce 5
# Consume 10
# last is 10
