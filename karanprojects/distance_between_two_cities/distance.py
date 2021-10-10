from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import lonlat, distance
import argparse


geolocator = Nominatim(user_agent="test")

# setting up arg parse
parser = argparse.ArgumentParser(description="Returns the distance between two cities")
parser.add_argument('city1',type=str,help="Name of first city")
parser.add_argument('city2',type=str,help="Name of second city")
parser.add_argument('units',type=str,help="Enter the Units (km,m,miles)")
args = parser.parse_args()


def Locator(loc1,loc2):
    location1 = geolocator.geocode(loc1)
    location2 = geolocator.geocode(loc2)
    return [(location1.latitude,location1.longitude),(location2.latitude,location2.longitude)]


def Distance(loc1,loc2,unit):
    if unit == "km":
        return distance(lonlat(*loc1),lonlat(*loc2)).km
    elif unit == "mi":
        return distance(lonlat(*loc1),lonlat(*loc2)).mi
    elif unit == "m":
        return distance(lonlat(*loc1),lonlat(*loc2)).m
    else:
        raise NotImplementedError

if __name__ == "__main__":
    loc1 = args.city1
    loc2 = args.city2
    unit = args.units
    x = Locator(loc1,loc2)
    print(Distance(x[0],x[1],unit))
