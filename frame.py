# Main alpha class
import pandas as pd
from numpy import unique


class factor():
    strate = None

    def __init__(self, space = 'US'):
        self.space = space
        
    def get_data(self, addr = None):
        # here the input is highly structed data file
        self.file_addr = addr
        if (type(self.file_addr) == str) & \
           (self.file_addr[-4:] == '.csv'):
            self.data = pd.read_csv(self.file_addr)
        else:
            assert (type(self.file_addr) == str), "Input obj.file_addr is not str"
            assert (self.file_addr[-4:] == '.csv'), "Data type not .csv"
            # assert (True), "Data type not supported"

    def data_rearrange(self):
        # date_list = unique(self.data[''])
        pass

    def backtest(self):
        pass


class low_vol(factor):
    strate = 'Low Volatility'
    # basic idea is to create a data-INDEPENDENT
    # method collections
    pass
