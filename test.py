from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from math import ceil

geolocator = Nominatim(user_agent="Mini-Projet")
depart = geolocator.geocode(input("Quelle est la ville de départ ? : "))
arriver = geolocator.geocode(input("Quelle est la ville d'arriver ? : "))


departcoord = (depart.latitude, depart.longitude)
arrivercoord = (arriver.latitude, arriver.longitude)

distance = int(geodesic(departcoord, arrivercoord).km)


def calcul(distance):

    temps = distance / 90
    heures = int(temps)
    minutes = int((temps-heures) * 60)
    freinaccel = 18 # Temps que prend le camion pour s'arreter et accelerrer 
    tempsdepause = 15

    pause = heures/2 + (freinaccel + tempsdepause)
        
    if minutes + pause >= 60:
        minutes = 0
        heures += 1

    return heures, ceil(minutes + pause),



print('La ville de départ est : ' + depart.address)

print('La ville de départ est : ' + arriver.address)

print('La distance parcouru est de : ' + str(distance) + ' km')

print('le temps pour parcourir cette distance est de : ' + str(calcul(distance)))