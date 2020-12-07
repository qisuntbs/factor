#!/usr/bin/env python3
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

import time


def run_test():
    from tests.test import test
    t = test("./tests/mlfdata.csv", "./tests/ret.csv")
    t.get_ret_panel(80)  # pick the first 80 stocks in the sample
    t.backtest()
    return t


if __name__ == '__main__':
    t = time.time()

    out = run_test()

    sample_ori_cov = out.cov_list[-200]
    sample_updated_cov = out.cov_list_post_shrinkage[-200]
    print(sample_ori_cov[0][:5])
    print(sample_updated_cov[0][:5])

    print(time.time() - t, 'seconds taken')
