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
    def cov(df):
        from cpp_wrap.cylink import cyfunc
        # calculate historical TS 36M covariance matrix
        # df - panel return data
        # df.shape = T * X (number of month * number of stocks)
        # np.cov(k)[0][0] = np.var(k[:,0], ddof=1)
        # with ddof to go from sample to population
        len_df = len(df)
        cov_list = []
        stock_list = []
        ret_list = []
        # remove those stocks that has no historical 36M returns
        for i in range(len_df - 36):
            sample = df.iloc[i:i+36, :]
            sample_t = np.array(sample).T
            non_nan_list = cyfunc().remove_nan(sample_t, 1)
            stock_list.append(non_nan_list)
            sample_non_nan = sample.iloc[:, non_nan_list]
            cov_list.append(np.cov(np.array(sample_non_nan).T))
            ret_list.append(sample_non_nan)
        return cov_list, stock_list, ret_list
