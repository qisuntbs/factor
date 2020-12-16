#!/usr/bin/env python3

import time
from factorbt.util import util
from tests import test_factor


def mlfactor():
    from tests.mlfactor import mlf_lv
    t = mlf_lv("./tests/mlfdata.csv", "./tests/ret.csv")
    t.get_ret_panel(80)  # pick the first 80 stocks in the sample
    t.backtest()
    return t


if __name__ == '__main__':
    # t = time.time()

    # out = mlfactor()
    # # cov = out.cov_list[0]
    # # cov_s = out.cov_list_post_shrinkage[0]
    # # from factorbt.risk import risk_model
    # # cov_mfm = risk_model.statistical(None, cov)
    # # print("cov:\n", cov[:5, :5])
    # # print("cov_mfm:\n", cov_mfm[:5, :5])
    # # print("cov_post_shrinkage:\n", cov_s[:5, :5])

    # from factorbt import util
    # y = out.weights[0]
    # x = list(range(len(y)))
    # inter = []
    # for i in y.keys():
    #     inter.append(y[i])
    # util.util.plot(x, inter)

    # print(time.time() - t, 'seconds taken')
    t = time.time()

    f, date_list, factor_name = test_factor.get_factor_data()

    cumulative_ret = [1.0]
    # cumulative_ic = [1.0]
    for i in range(len(f.FF_return_list)):
        cumulative_ret.append(cumulative_ret[i] *
                              (f.FF_return_list[i] + 1))
        # cumulative_ic.append(cumulative_ic[i] *
        #                      (f.factor_IC_list[i] + 1))

    util.plot(date_list, cumulative_ret[:-1],
              'cumu_ret',
              factor_name + ' Cumulative Returns',
              'line')
    # util.plot(date_list, cumulative_ic[:-1],
    #           'cumu_ic',
    #           factor_name + ' Cumulative IC',
    #           'line')
    util.plot(date_list, f.FF_return_list, 'default',
              factor_name + ' Monthly Return')
    util.plot(date_list, f.factor_IC_list, 'cumu_ic',
              factor_name + ' Monthly IC')

    print('IC Average:', sum(f.factor_IC_list) / len(f.factor_IC_list))
    print(time.time() - t, 'seconds taken')
