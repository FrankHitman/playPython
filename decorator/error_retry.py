import logging
import time
import sys
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


class A(object):
    def __init__(self):
        self.tt = 0

    @retry(3)
    def aa(self):
        self.tt += 1
        if self.tt < 3:
            logging.info(1)
            raise RuntimeError('error')
        logging.info('success')

if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    abj = A()
    abj.aa()

# @retry(2)
# 2021-09-24 16:12:12,625 - try 1
# 2021-09-24 16:12:12,626 - 1
# 2021-09-24 16:12:12,726 - try 2
# 2021-09-24 16:12:12,726 - 1
# 2021-09-24 16:12:12,826 - function aa retried 2 times, all failed: error

# @retry(3)
# 2021-09-24 16:25:14,514 - try 1
# 2021-09-24 16:25:14,515 - 1
# 2021-09-24 16:25:14,616 - try 2
# 2021-09-24 16:25:14,616 - 1
# 2021-09-24 16:25:14,717 - try 3
# 2021-09-24 16:25:14,717 - success
