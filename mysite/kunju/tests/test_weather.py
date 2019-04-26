"""
We cannot use assert statements here, since the weather summary is not constant everyday

If the output of running this test is
Example Output:

Minimum, Maximum and summary of Temperature on each day is  MIN: 63.11 MAX: 63.11 Summary: Partly cloudy throughout the day.
Minimum, Maximum and summary of Temperature on each day is  MIN: 63.03 MAX: 63.03 Summary: Partly cloudy throughout the day.


Compare the results in the web page "Weather Summary Section" by entering following details
Location: Minnesota
From date: 2019-08-01
To date: 2019-08-02

If this function worked properly, then we should see the same result in terminal and Webpage

"""




import unittest
from kunju.weather import getsummary
from datetime import datetime



class Testweather(unittest.TestCase):
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

