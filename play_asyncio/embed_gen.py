def sub_gen1(x):
    r = yield x
    print('subgen1', r)


def gen1(x):
    r = yield sub_gen1(x)
    print('gen1', r)


g = gen1(3)
g.send(None)
g.send(21)


# g = gen1(3)
# g
# <generator object gen1 at 0x10f9ce450>
# g.send(None)
# <generator object sub_gen1 at 0x10f9ce3d0>
# g.send(21)
# gen1 21
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

def sub_gen2(x):
    r = yield x
    print('subgen2', r)
    return x + 10


def gen2(x):
    r = yield from sub_gen2(x)
    print('gen2', r)


g2 = gen2(2)
g2.send(None)
g2.send(9)

# g2=gen2(2)
# g2.send(None)
# 2
# g2.send(100)
# subgen2 100
# gen2 12
