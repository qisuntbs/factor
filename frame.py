# Main factor backtesting classes
import pandas as pd
from pypfopt import EfficientFrontier
from funcs.calc import data_manipulate, calc


class factor():
    def __init__(self, space='US'):
        self.space = space
        self.strate = None  # strategy
        self.weights = []
        
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

    def cov_shrinkage(self, delta=0.2):
        from funcs.calc import calc
        # TODO: implement more advanced shrinkage methods using pypfopt
        # http://www.ledoit.net/honey.pdf
        assert (hasattr(self, "cov_list")), "looking for attribute 'cov_list'"
        self.delta = delta
        self.cov_list_post_shrinkage = []
        for cov in self.cov_list:
            self.cov_list_post_shrinkage.append(calc.shrunk_covariance(cov, self.delta))


class low_vol(factor):
    def lv_backtest(self):
        self.strate = "Low Volatility"

        for i in range(len(self.cov_list)):
            sample_cov = pd.DataFrame(self.cov_list[i])
            df = self.ret_list[i]
            mu = df.mean()
            ef = EfficientFrontier(mu, sample_cov)
            self.weights.append(ef.min_volatility())
            # self.weights.append(ef.max_sharpe())

        # if hasattr(self, "cov_list"):
        #     # df = pd.DataFrame(self.stock_list[0])
        #     # self.cov_sample = risk_models.sample_cov(df)
        #     self.ef = EfficientFrontier(0, self.cov_list[0])
        # else:
        #     assert (False), "run panel_cov to get cov/stock/ret_list"


class single_factor(factor):
    pass


class multi_factor(factor):
    pass
