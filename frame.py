# Main alpha class
import pandas as pd
from funcs.calc import data_manipulate, calc


class factor():
    strate = None

    def __init__(self, space='US'):
        self.space = space
        
    def get_data(self, addr=None):
        # here the input is highly structed data file
        self.file_addr = addr
        if (type(self.file_addr) == str) & \
           (self.file_addr[-4:] == '.csv'):
            self.data = pd.read_csv(self.file_addr)
        else:
            assert (type(self.file_addr) == str), "Input obj.file_addr is not str"
            assert (self.file_addr[-4:] == '.csv'), "Data type not .csv"
            # assert (True), "Data type not supported"

    def data_rearrange(self, col_list) -> None:
        self.df = self.data[col_list]
        self.df_list = data_manipulate.re_arrange(self.data)

    def panel_cov(self) -> None:
        if hasattr(self, "ret_data"):
            cov_list, stock_list, ret_list = calc.cov(self.ret_data)
            self.cov_list = cov_list  # cov_list generated
            self.stock_list = stock_list  # stock_list generated
            self.ret_list = ret_list # return_list generated
        else:
            assert (False), "looking for attribute 'ret_data'"


class low_vol(factor):
    strate = 'Low Volatility'
    weights = []

    def lv_backtest(self):
        from pypfopt import EfficientFrontier

        for i in range(len(self.cov_list)):
            sample_cov = pd.DataFrame(self.cov_list[i])
            df = self.ret_list[i]
            mu = df.mean()
            ef = EfficientFrontier(mu, sample_cov)
            self.weights.append(ef.min_volatility())
            # self.weights.append(ef.max_sharpe())

        # x = []
        # y = []
        # i = 0
        # import math
        # for key, value in self.weights.items():
        #     if value > 0.0001:
        #         i += 1
        #         x.append(i)
        #         y.append(value)
        #     if math.isnan(value):
        #         print(value)
        # util.plot(x, y)
        # print(i, "stocks in the portfolio")

        # if hasattr(self, "cov_list"):
        #     # df = pd.DataFrame(self.stock_list[0])
        #     # self.cov_sample = risk_models.sample_cov(df)
        #     self.ef = EfficientFrontier(0, self.cov_list[0])
        # else:
        #     assert (False), "run panel_cov to get cov/stock/ret_list"

    def cov_shrinkage(self):
        # TODO: implement basic covariance shrinkage
        pass


class single_factor_test(factor):
    pass


class multi_factor_opt(factor):
    pass
