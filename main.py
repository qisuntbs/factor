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
    cov = out.cov_list[0]
    cov_s = out.cov_list_post_shrinkage[0]
    from factorbt.risk import risk_model
    cov_mfm = risk_model.statistical(None, cov)
    print("cov:\n", cov[:5, :5])
    print("cov_mfm:\n", cov_mfm[:5, :5])
    print("cov_post_shrinkage:\n", cov_s[:5, :5])

    print(time.time() - t, 'seconds taken')
