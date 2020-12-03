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
