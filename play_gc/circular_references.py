# encoding=utf-8

class A(object):
    def __init__(self, b_instance):
        self.b = b_instance


class B(object):
    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print("die")


# def test():
#     b = B()


import gc

gc.collect()
print(gc.garbage)


def test():
    b = B()
    import objgraph
    objgraph.show_backrefs([b, b.a], refcounts=True)


test()
