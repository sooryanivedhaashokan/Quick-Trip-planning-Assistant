from darksky import forecast
key= 'd3da5d302715a03911052960bc5d3087'
from datetime import datetime
from datetime import timedelta
import statistics

class weather():
    def __init__(self, min_temp, max_temp, summary, f):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.summary = summary
        self.f = f

def getsummary(lati, longi,f ,t):
    summary = []
    while f <= t:
        ke = key, lati, longi
        temp = forecast(*ke, time=datetime.combine(f, datetime.min.time()).isoformat())
        s = temp['daily']['data'][0]
        w = weather(str(s['temperatureMin']), str(s['temperatureMax']), str(s['summary']), str(f))
        summary.append(w)
        summ = str(f) + ' - ' + '  Min: ' + str(s['temperatureMin']) + '  Max: ' + str(s['temperatureMax']) \
            + '  Summary  : ' + s['summary']
        f = f + timedelta(days=1)
    return summary


