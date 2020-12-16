# this file collects a range of calculations this multi-factor framework needs:
# Data Manipulations
# Numerical Calculations

import pandas as pd
import numpy as np


class data_manipulate():
    @staticmethod
    def re_arrange(df):
        # input data check:
        assert (type(df) == pd.core.frame.DataFrame), "Input has to be pandas.DF"
        assert (('date' in df.columns) | ('Date' in df.columns)),\
            "No Col named 'date' or Date"

        # core calucation:
        if 'date' in df.columns:
            col_date = 'date'
        elif 'Date' in df.columns:
            col_date = 'Date'
        date_list = np.unique(df[col_date])

        df_reshape = []
        for i in range(len(date_list)):
            inter = df.loc[df[col_date] == date_list[i]]
            df_reshape.append(inter)
        return df_reshape


class calc():
    @staticmethod
    def cov(df, number_of_periods=36):
        from cpp_wrap.cylink import cyfunc
        # calculate historical 36M (default) covariance matrix
        # df - panel return data
        # df.shape = T * X (number of month * number of stocks)
        # np.cov(k)[0][0] = np.var(k[:,0], ddof=1)
        # with ddof to go from sample to population
        len_df = len(df)
        cov_list = []
        stock_list = []
        ret_list = []
        # remove those stocks that has no historical 36M returns
        for i in range(len_df - number_of_periods):
            sample = df.iloc[i:i+number_of_periods, :]
            sample_t = np.array(sample).T
            non_nan_list = cyfunc().remove_nan(sample_t, 1)
            stock_list.append(non_nan_list)
            sample_non_nan = sample.iloc[:, non_nan_list]
            cov_list.append(np.cov(np.array(sample_non_nan).T))
            ret_list.append(sample_non_nan)
        return cov_list, stock_list, ret_list

    @staticmethod
    def shrunk_covariance(cov, delta):
        # native covariance shrinkage
        N = cov.shape[1]
        mu = np.trace(cov) / N  # average of the matrix diagonals
        F = np.identity(N) * mu
        shrunk_cov = delta * F + (1 - delta) * cov
        return shrunk_cov

    @staticmethod
    def port_sort_ret(df, factor, high_minus_low=True):
        assert (type(df) == pd.DataFrame), "Looing for pd.DataFrame"
        assert ('ret' in list(df.columns)), "missing col named 'ret'"
        # sort the fundamental data to perform the test
        # df represents cross-sectional data at
        # ONE time point
        stock_num = len(df)
        pick_num = int(stock_num / 10 * 3)

        sort_ind = True if high_minus_low is False else False

        df = df.sort_values(by=factor, ascending=sort_ind)
        # Fama-French 3/4/3 or 1/8/1 high-low return:
        FF_return = df['ret'].iloc[:pick_num].mean() - \
            df['ret'].iloc[-pick_num:].mean()
        # full-sample ranking IC:
        ret_order = np.array(df['ret']).argsort()[::-1].argsort()
        FF_IC = np.corrcoef(np.array(range(len(df))),
                            ret_order)[0, 1]
        return FF_return, FF_IC
