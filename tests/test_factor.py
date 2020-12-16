#!/usr/bin/env python3
# import unittest
import numpy as np
import pandas as pd
from factorbt.frame import single_factor
from cpp_wrap.cylink import cyfunc


def get_factor_data():
    f = single_factor()
    f.get_data("./tests/mlfdata.csv")
    ori = f.data
    # inter = ori.loc[(ori['date'] > '1999-12-31') &
    #                 (ori['date'] <= '2018-12-31')]
    inter = ori.loc[(ori['date'] > '2000-12-31') &
                    (ori['date'] <= '2020-12-31')]
    data = inter[['date',
                  'stock_id',
                  'Pb',  # value ok
                  'Mom_11M_Usd',  # Momentum X
                  'Fcf_Toa',  # quality X
                  'Vol3Y_Usd',  # vol X
                  'Mkt_Cap_3M_Usd',  # size ok
                  'R1M_Usd',
                  'R3M_Usd',
                  'R6M_Usd',
                  'R12M_Usd']]
    col_list = list(data.columns[1:])

    for i in range(len(col_list)):
        if col_list[i] == 'R1M_Usd':
            col_list[i] = 'ret'
    data.index = list(data['date'])
    data = data.drop(data.columns[0], axis=1)

    date_list = list(set(list(data.index)))
    date_list.sort()
    data_list = []
    for i in date_list:
        inter = np.array(data.loc[data.index == i])
        non_nan_list = cyfunc().remove_nan(inter, 1)
        inter_pd = pd.DataFrame(inter[non_nan_list, :],
                                columns=col_list)
        inter_pd['stock_id'] = inter_pd['stock_id'].astype(int)
        data_list.append(inter_pd)

    f.insert_data_list(date_list, data_list)
    factor_name = col_list[1]
    high_minus_low = False
    f.hml(factor_name, high_minus_low)
    # for take negative return for the size factor (SMB)
    return f, date_list, factor_name
