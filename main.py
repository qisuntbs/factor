#!/usr/bin/python3

import time


def run_test():
    from tests.test import test
    t = test('./tests/mlfdata.csv')
    t.get_ret_panel()
    t.get_cov()
    return t


if __name__ == '__main__':
    t = time.time()

    t1 = run_test()
    # print(t1.data.iloc[-5:, :10])

    print(time.time() - t, 'seconds taken')
