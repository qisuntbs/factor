# This is the main script to load a full-sample data
# and generate multiple factor-based results
# data: http://www.mlfactor.com/factor.html

from factorbt.frame import low_vol


class mlf_lv(low_vol):
    def __init__(self, file_addr=None, ret_file_addr="./tests/ret.csv"):
        import os.path

        self.ret_file_addr = ret_file_addr
        if os.path.exists(ret_file_addr):
            self.file_addr = file_addr
        else:
            self.get_data(file_addr)

        self.strate = None
        self.weights = []

    def get_ret_panel(self, number_of_stock=None) -> None:
        # update data to panel returns
        from factorbt.util import util

        if hasattr(self, "data"):
            print("obj has attribute 'data'")
            inter = self.data[['stock_id', 'date',
                               'R1M_Usd', 'R3M_Usd',
                               'R6M_Usd', 'R12M_Usd']]
            inter = inter.rename(columns={'R1M_Usd': 'ret'})
            future_ret = util.data_to_panel(inter, self.ret_file_addr)
        else:
            future_ret = util.data_to_panel(None, self.ret_file_addr)
        date_list = list(future_ret.iloc[:, 0])
        date_list.append('2019-04-30')
        date_list_t0 = date_list[1:]
        future_ret.index = date_list_t0
        future_ret = future_ret.drop(future_ret.columns[0], axis=1)
        # self.ret_data = future_ret
        if number_of_stock is None:
            print("Caution - you have chosen full-sample data")
            self.ret_data = future_ret
        elif number_of_stock > 10:
            print("We select the sample of the first", number_of_stock, "stocks only")
            self.ret_data = future_ret.iloc[:, :number_of_stock]
        else:
            assert (False), "10 or more stocks"

    def backtest(self) -> None:
        # import numpy as np
        self.panel_cov()
        self.riskmodel()
        self.cov_shrinkage(0.2)  # shrinkage parameter: 0.2
        self.lv_backtest()
