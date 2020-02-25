import ephem # модуль для определения в каком созвездии находится планета на определенную дату

planets = {'Mars': ephem.Mars, 'Mercury': ephem.Mercury, 'Venus': ephem.Venus, 'Jupiter': ephem.Jupiter, 'Saturn': ephem.Saturn,
       'Uranus': ephem.Uranus, 'Neptune': ephem.Neptune, 'Pluto': ephem.Pluto, 'Sun': ephem.Sun, 'Moon': ephem.Moon
       }

planet_name = 'Venus'
planet_method = planets[planet_name]
planet_sozvezdie = planet_method(ephem.now())
print(planet_sozvezdie)

#mars = planets['Mars]('2000/01/01')
#print(mars)

#print(ephem.Mars('2000/01/01'))