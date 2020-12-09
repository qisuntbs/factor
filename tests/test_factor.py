#!/usr/bin/env python3

import unittest
from factorbt.frame import factor


class TestFactorFrame(unittest.TestCase):
    def test_data(self):
        f = factor()
        f.get_data("./tests/ret.csv")
        self.assertEqual(len(f.data), 245)


if __name__ == '__main__': 
    unittest.main() 
