#!/usr/bin/python3


import time
from frame import factor
from funcs.util import util


if __name__ == '__main__':
    t = time.time()

    a = factor('CA')
    print(a.__dict__)

    util.plot(list(range(5)), [ 5, 4,5,3,4])

    print(time.time() - t, 'seconds taken')
