#
# Title:test_target.py
# Description:
# Development Environment:OS X 10.13.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import unittest

from target import Target

class TargetTest(unittest.TestCase):

    def test_00(self):
        target = Target()
        self.assertEquals(5, target.adder(2, 3))

#
if __name__ == '__main__':
    unittest.main()