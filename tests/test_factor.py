#!/usr/bin/env python3

import unittest
from frame import factor


class TestFactorFrame(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__': 
    unittest.main() 
