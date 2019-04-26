"""
We cannot use assert statements here, since the air fares are not constant everyday

If the output of running this test is
Example Output:

In the Airport LONDON/GB:HEATHROW: Airline with cheapest fare is BRITISH AIRWAYS => fare $829.96
In the Airport LONDON/GB:GATWICK: Airline with cheapest fare is NORWEGIAN AIR UK => fare $377.51

Compare the results in the web page "Cheapest Flight Details Departure Section" by entering following details
Location: London
From date: 2019-08-10
To date: any

If this function worked properly, then we should see the same result in terminal and Webpage

"""


import unittest
from kunju.flight import getcheapestflights

class Testflight(unittest.TestCase):
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



