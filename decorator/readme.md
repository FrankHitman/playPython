# Python Decorator

### 简单认识
由于函数（function）也是一个对象，而且函数对象可以被赋值给变量，函数可以作为另一个函数的变量。
装饰器一般作用是将原有函数添加上新的一些功能，然后将新的功能更强的函数返回

```python
import time

def time_cost(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        func(*args, **kwargs)
        cost = (time.time() - s) * 1000
        print('time cost: {} ms'.format(int(cost)))
        return
    return wrapper
```

使用
```
@time_cost
def stop():
    pass

# 以上语法糖等同于以下代码
def stop():
    pass
new_stop = time_cost(stop)
# new_stop 还是一个函数，一个对象，还是可以通过new_stop()进行调用
```

### 装饰器本身带有参数
如下就是一个错误重试的装饰器，而每个函数的重试次数可以在定义的时候单独指定。
```
from functools import wraps


def retry(times):
    def wrapper_fn(f):
        @wraps(f)
        def new_wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    logging.info('try %s' % (i + 1))
                    return f(*args, **kwargs)
                except Exception as e:
                    if i < 5:
                        time.sleep(0.1)
                    else:
                        time.sleep(1)
                    error = e
            # here ignore exception
            logging.error('function {} retried {} times, all failed: {}'.format(f.__name__, times, error))

        return new_wrapper

    return wrapper_fn

```
使用
```
@retry(3)
def start():
    pass
# 等同于
new_start = retry(3)(start)
# new_start 还是一个函数，还是可以通过new_start()进行调用
```

以上装饰器中使用了一个装饰器`functools.wraps`，用来消除装饰器对原来函数的属性的修改。
通过打印 `stop.__name__` 和 `start.__name__` 得知。
==> wrapper    和    start

### 装饰器应用于类的方法（method）
如果要给类的方法加上装饰器怎么办？

如果在方法执行出错超过一定次数的时候执行类的另外一个方法，以达到兜底作用，例如给其他模块发出错信息。该怎办？

```python
import logging
import time
import sys
from functools import wraps

def retry(times, func_name):
    def wrapper_fn(f):
        @wraps(f)
        def new_wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    if i < 5:
                        time.sleep(0.1)
                    else:
                        time.sleep(1)
                    error = e
            # here ignore exception
            logging.error('function {} retried {} times, all failed: {}'.format(f.__name__, times, error))
            final_func = getattr(args[0], func_name)
            final_func()

        return new_wrapper

    return wrapper_fn


class A(object):
    def __init__(self):
        self.tt = 0

    @retry(3, 'as_decorator_parameter')
    def aa(self):
        self.tt += 1
        if self.tt < 5:
            logging.info(1)
            raise RuntimeError('get value failed')
        logging.info('success')

    def as_decorator_parameter(self):
        logging.info(self.tt)
        logging.info('in decorator parameter')

```

通常类方法的第一个参数是self，也就是类的实例化后的一个实例本身.

以上通过python内置函数`getattr(args[0], func_name)`获取到实例的方法，并执行之。

#### 补充下 *args & **kwargs
*args (Non Keyword Arguments) 和 **kwargs (Keyword Arguments)
```
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
```
```
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
```

### reference
- [python3-cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p01_put_wrapper_around_function.html)
- [args-and-kwargs](https://www.programiz.com/python-programming/args-and-kwargs)
- [闭包与functools.wraps](https://zhuanlan.zhihu.com/p/78500405)
- [eval](https://www.programiz.com/python-programming/methods/built-in/eval)
