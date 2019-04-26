from amadeus import Client, ResponseError, Location
import sys

api = '9QDVsLDcHslhtzYEzzEW0SI70LN6QoNG'
sec = 'cYOhthhAtL4mJ2Ga'

amadeus = Client(client_id=api, client_secret=sec)



class cheapairfares():
    def __init__(self, price, arrival, departure, airline, arrival_name, depart_name, arrival_time, departure_time):
        self.price = price
        self.arrival = arrival
        self.departure = departure
        self.airline = airline
        self.arrival_name = arrival_name
        self.depart_name = depart_name
        self.arrival_time = arrival_time
        self.departure_time = departure_time
    def getvalues(self):
        return self.arrival_name + "    "+self.depart_name + "    " + self.price  + "  " + self.airline

class minfare():
    def __init__(self, price, arrival, departure, airline, arrival_name, depart_name):
        self.price = price
        self.airline = airline
        self.arrival_name = arrival_name
        self.depart_name = depart_name


def getcheapestflights(orig,des,f):
    flights = []

    try:

         # Flight Low-fare Search
         response = amadeus.shopping.flight_offers.get(origin=orig, destination=des, departureDate=f) 
         s = response.data
         length_s = str(len(s))
         print("Total Number of flights operating between " + orig + " and " + des + " is " + length_s)
         for i in range(len(s)):
             if len(s[i]['offerItems'][0]['services'][0]['segments']) == 1:
                 price = s[i]['offerItems'][0]['price']['total']
                 arrival = s[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['arrival']['iataCode']
                 departure = s[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['departure']['iataCode']
                 arrival_time = s[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['arrival']['at']
                 departure_time = s[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['departure']['at']
                 ac = s[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['operating']['carrierCode']
                 airline =  amadeus.reference_data.airlines.get(airlineCodes=ac)
                 airline_name = airline.data[0]['businessName']
                 a_airport_r = amadeus.reference_data.locations.get(keyword=arrival, subType=Location.AIRPORT)
                 d_airport_r = amadeus.reference_data.locations.get(keyword=departure, subType=Location.AIRPORT)
                 arrival_name = a_airport_r.data[0]['detailedName']
                 depart_name = d_airport_r.data[0]['detailedName']
                 cheaps = cheapairfares(price,arrival, departure,airline_name, arrival_name, depart_name, arrival_time, departure_time)
                 flights.append(cheaps)

             if (i >= 10):
                 break
         length_flights = str(len(flights))
         print("Number of direct flights between " + orig + " and " + des + " is " + length_flights)

    except ResponseError as error:
         print(error)
    first = sys.float_info.max
    min_fare = []
    for item in flights:
        if (float(item.price) < first):
            first = float(item.price)
            min_fare.clear()
            min_fare.append(item)

    if len(min_fare) > 0:
        return min_fare[0]



#    print(item.departure)

#print(getcheapestflights('LON', '2019-08-10'))


