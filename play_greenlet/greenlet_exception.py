# encoding=utf-8
#
# from greenlet import greenlet
#
# def test1():
#     print 12
#     gr2.throw(greenlet.GreenletExit)
#     try:
#         gr2.switch()
#     except greenlet.GreenletExit:
#         print 90
#     print 34
#
# def test2():
#     print 56
#     raise greenlet.GreenletExit
#     print 78
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2, gr1)
# gr1.switch()
# print 78

# 既然协程是存放在栈中，那一个协程要抛出异常，就会先抛到其父协程中，如果所有父协程都不捕获此异常，程序才会退出。
# 12
# 56
# 90
# 34
# 78

# 有一个异常是特例，不会被抛到父协程中，那就是”greenlet.GreenletExit”，这个异常会让当前协程强制退出
# 12
# 56
# 34
# 78


from greenlet import greenlet

def test1():
    print 12
    try:
        gr2.throw(NameError)
        gr2.switch()
    except NameError:
        print 90
    print 34

def test2():
    print 56
    # raise NameError

gr1 = greenlet(test1)
gr2 = greenlet(test2, gr1)
gr1.switch()
print 78