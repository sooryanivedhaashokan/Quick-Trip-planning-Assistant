"""
This test will make sure that every time when this function is called, we get the same results for the latitude and
longitude with respect to the location entered
"""
import unittest
from kunju.geolocate import lati, longi

class TestAir(unittest.TestCase):
	def test_lati(self):
		result_lati = lati('New York')
		result_longi = longi('New York')
		self.assertEqual(result_lati,40.7127281)
		self.assertEqual(result_longi,-74.0060152)