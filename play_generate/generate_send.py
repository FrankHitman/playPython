def count(n):
    x = 0
    while x < n:
        value = yield x
        if value is not None:
            print('Received value: %s' % value)
        x += 1


gen = count(5)
# print gen
# print gen.next()
print(gen.send(None))
print(gen.send('hello'))
