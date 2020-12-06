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

    print(time.time() - t, 'seconds taken')
    # for i in range(len(t1.cov_list)):
    #     print(t1.cov_list[i].shape[0])
