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
        # calculate historical TS 36M co-variance matrix
        # df - panel return data
        # df.shape = T * X (number of month * number of stocks)
        # np.cov(k)[0][0] = np.var(k[:,0], ddof=1)
        # with ddof to go from sample to population
        len_df = len(df)
        cov_list = []
        # TODO remove those stocks that has no historical returns
        for i in range(len_df - 35):
            sample = df.iloc[i:i+36, :]
            cov_list.append(np.cov(sample.to_numpy().T))
        return cov_list
