# -*- coding: utf-8 -*-
#
# Copyright (C) 2019, 2020 by Qi Sun
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
from pypfopt import EfficientFrontier
from factorbt.calc import data_manipulate, calc
from factorbt.risk import risk_model


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
            self.ret_list = ret_list  # return_list generated
        else:
            assert (False), "looking for attribute 'ret_data'"

    def riskmodel(self, model_type="Statistical", K=7):
        # bad name
        self.cov_list_mfm = []
        if model_type == "Statistical":
            for cov in self.cov_list:
                self.cov_list_mfm.append(risk_model.statistical(None, cov, K))
        elif model_type == "Fundamental":
            for i in range(len(self.ret_list)):
                self.cov_list_mfm.append(risk_model.fundamental(self.ret_list[i],
                                                                self.cov_list[i]))
        else:
            assert (False), "Please specify the type of the risk model"

    def cov_shrinkage(self, delta=0.2):
        # TODO: implement more advanced shrinkage methods using pypfopt
        # http://www.ledoit.net/honey.pdf
        assert (hasattr(self, "cov_list")), "looking for attribute 'cov_list'"
        self.delta = delta
        self.cov_list_post_shrinkage = []
        for cov in self.cov_list_mfm:
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


class single_factor(factor):
    def insert_data_list(self, date_list, data_list):
        self.date_list = date_list
        self.data_list = data_list

    def hml(self, factor, high_minus_low):
        # 1) Fama_French high-low equally weighted returns
        # 2) single factor cumulative IC
        self.FF_return_list = []
        self.factor_IC_list = []
        for i in self.data_list:
            ff_ret, ic = calc.port_sort_ret(i, factor, high_minus_low)
            self.FF_return_list.append(ff_ret)
            self.factor_IC_list.append(ic)


class multi_factor(factor):
    pass
