# this file collects a range of uitility functions this multi-factor framework needs

import os.path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class util():
    @staticmethod
    def plot(x, y, file_name='default'):
        assert ((type(x) == list) & (type(x) == list)), "Plot inputs have to be lists" 
        assert (len(x) == len(y)), "x-axis & y-axis need to be equally numbered"
        # plot to pdf file:
        f = plt.figure()
        plt.plot(x, y, 'o')
        f.savefig("./plots/" + file_name + ".pdf", bbox_inches="tight")

    @staticmethod
    def data_to_panel(df, file_addr=None):
        # this is the funciton to reshape the original data
        # to a date * ret 2D panel
        if os.path.exists(file_addr):
            out = pd.read_csv(file_addr)
        else:
            assert (('date' in df.columns) & ('ret' in df.columns)), "Need date and ret"
            date_list = list(set(df['date']))
            date_list.sort()
            stock_list = list(set(df['stock_id']))
            stock_list.sort()
            # Extremely slow - 2500 seconds taken
            out = pd.DataFrame(np.nan, index=date_list,
                               columns=stock_list)
            for i in range(len(date_list)):
                for j in range(len(stock_list)):
                    inter = df.loc[(df['date'] == date_list[i]) &
                                   (df['stock_id'] == stock_list[j])]
                    if len(inter) == 1:
                        out.at[date_list[i], stock_list[j]] = inter['ret'].iloc[0]
                    else:
                        assert (len(inter) < 2), "Fatal Error in funcs.util.data_to_panel"
            # trying Cython:
            out.to_csv(file_addr)
        return out

    # @staticmethod
    # def nparray_to_df(nparray):
    #     assert (isinstance(nparray, np.ndarray)), "input type must be np.ndarray"
    #     return pd.DataFrame(nparray)
