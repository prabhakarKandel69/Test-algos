import math

def haversine(lat1,long1,lat2,long2):
    lat1 = math.radians(round(lat1,6))
    lat2 = math.radians(round(lat2,6))
    long1 = math.radians(round(long1,6))
    long2 = math.radians(round(long2,6))


    r = 6371
    dellat = lat2 - lat1
    dellong = long2 - long1

    sine_lat = math.sin(dellat/2) ** 2
    sine_long = math.sin(dellong/2) ** 2

    cos_1 = math.cos(lat1)
    cos_2 = math.cos(lat2)

    dist = 2 * r * math.asin(math.sqrt(sine_lat + cos_1 * cos_2* sine_long))
    return 1.3*dist


    

