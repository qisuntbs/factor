#!/usr/bin/python3

import time


def run_test():
    from tests.test import test
    t = test('./tests/mlfdata.csv')
    t.get_ret_panel()
    return t


if __name__ == '__main__':
    t = time.time()

    t1 = run_test()

    print(time.time() - t, 'seconds taken')
