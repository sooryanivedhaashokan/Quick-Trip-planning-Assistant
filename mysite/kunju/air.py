from amadeus import Client, ResponseError

api = '9QDVsLDcHslhtzYEzzEW0SI70LN6QoNG'
sec = 'cYOhthhAtL4mJ2Ga'

amadeus = Client(client_id=api, client_secret=sec)



def getnearestairports(lat, long):
    airports = {}
    try:
        response = amadeus.reference_data.locations.airports.get(
            longitude=long, latitude=lat)

        for i in range(3):
                code = response.data[i]['address']
                name = response.data[i]['name']
                iataCode = response.data[i]['iataCode']

                check = code['cityCode']
                airports[name] = iataCode
                if i >= 3:
                    break
    except ResponseError as error:
            print(error)
    # print(airports)
    return airports


s= getnearestairports(51.50,-0.12)
print(s)
