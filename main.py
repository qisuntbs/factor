#!/usr/bin/env python3

import time


def mlfactor():
    from tests.mlfactor import mlf_lv
    t = mlf_lv("./tests/mlfdata.csv", "./tests/ret.csv")
    t.get_ret_panel()  # pick the first 80 stocks in the sample
    t.backtest()
    return t


if __name__ == '__main__':
    t = time.time()

    out = mlfactor()

    sample_ori_cov = out.cov_list[-200]
    sample_cov_mfm = out.cov_list_mfm[-200]
    sample_updated_cov = out.cov_list_post_shrinkage[-200]

    N = 3
    print(sample_ori_cov[:N][:N])
    print(sample_cov_mfm[:N][:N])
    print(sample_updated_cov[:N][:N])

    print(time.time() - t, 'seconds taken')
