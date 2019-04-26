import unittest
from kunju.air import getnearestairports
from kunju.geolocate import lati, longi
from kunju.flight import getcheapestflights
from kunju.weather import getsummary
from datetime import datetime



class TestAll(unittest.TestCase):
	def test_getnearestairports(self):
		result = getnearestairports(40.73,-73.93)
		self.assertEqual(result,{'NEWARK LIBERTY INTL': 'EWR', 'LAGUARDIA': 'LGA', 'JOHN F KENNEDY INTL': 'JFK'})

	def test_lati(self):
		result_lati = lati('New York')
		result_longi = longi('New York')
		self.assertEqual(result_lati,40.7127281)
		self.assertEqual(result_longi,-74.0060152)


	def test_getcheapestflights(self):
		airports = {'GATWICK': 'LGW', 'HEATHROW': 'LHR', 'CITY AIRPORT': 'LCY'}
		min_fares = []
		for key, value in airports.items():
			print(key + "=>" + value)
			flights = getcheapestflights('JFK', value, '2019-08-10')
			min_fares.append(flights)

		for item in range(len(min_fares)):
			if min_fares[item] is not None:
				print("In the Airport " +min_fares[item].arrival_name + ": Airline with cheapest fare is " + min_fares[item].airline + " => fare " + "$"+min_fares[item].price)
		if not min_fares: return False
		return True
	

	def test_getsummary(self):
	        f = datetime.strptime('2019-08-01', '%Y-%m-%d')
	        t = datetime.strptime('2019-08-02', '%Y-%m-%d')
	        lati = 45.98
	        longi = -94.61
	        summary = getsummary(lati, longi, f, t)
	
	        for item in range(len(summary)):
	            if summary[item] is not None:
	                print("Minimum, Maximum and summary of Temperature on each day is " + " MIN: " + summary[item].min_temp
	                      + " MAX: " + summary[item].min_temp + " Summary: " + summary[item].summary)
	        if not summary: return False
	        return True
