# to run unittest:
# python3 -m unittest

import unittest
from factorbt.frame import factor


def get_factor():
    f = factor()
    f.get_data("./tests/ret.csv")
    N = 20
    ret_data = f.data
    date_list = ret_data.iloc[:, 0]
    ret_data.drop(ret_data.columns[0], axis=1, inplace=True)
    ret_data.index = list(date_list)
    f.ret_data = ret_data.iloc[:, :N]
    f.panel_cov()
    f.riskmodel()
    f.cov_shrinkage()
    return f


class TestFactorFrame(unittest.TestCase):
    def test_ret_data(self):
        f = get_factor()
        target_len = 245
        self.assertEqual(len(f.ret_data), target_len)

    def test_cov(self):
        # TODO:
        # Test statistical risk model
        f = get_factor()
        self.assertEqual(len(f.cov_list),
                         len(f.cov_list_post_shrinkage))
        for i in range(len(f.cov_list)):
            self.assertEqual(f.cov_list[i].shape,
                             f.cov_list_post_shrinkage[i].shape)
