from geopy.geocoders import Nominatim

def lati(location):
    geolocator = Nominatim(scheme='http')
    l = geolocator.geocode(location)
    return l.latitude

def longi(location):
    geolocator = Nominatim(scheme='http')
    l = geolocator.geocode(location)
    return l.longitude

print(longi('New York'))
print(lati('New york'))