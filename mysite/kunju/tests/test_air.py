"""
This test will make sure that every time when this function is called, we get the same results for the latitude and
longitude entered
"""

import unittest
from kunju.air import getnearestairports

class TestAir(unittest.TestCase):
	def test_getnearestairports(self):
		result = getnearestairports(40.73,-73.93)
		self.assertEqual(result,{'NEWARK LIBERTY INTL': 'EWR', 'LAGUARDIA': 'LGA', 'JOHN F KENNEDY INTL': 'JFK'})
