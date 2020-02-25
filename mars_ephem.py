import ephem # модуль для определения в каком созвездии находится планета на определенную дату

mars = ephem.Mars('2000/01/01') # определяет где находится Mars по дате 2000/01/01
print(mars)

const = ephem.constellation(mars) # определяет созвездие для переменной mars (constellation - это атрибут модуля ephem)
print(const)

planet_dct = {'Mars': ephem.Mars,

              }

dct = {'Mars': ephem.Mars, 'Mercury': ephem.Mercury, 'Venus': ephem.Venus, 'Jupiter': ephem.Jupiter, 'Saturn': ephem.Saturn,
       'Uranus': ephem.Uranus, 'Neptune': ephem.Neptune, 'Pluto': ephem.Pluto, 'Sun': ephem.Sun, 'Moon': ephem.Moon
       }

sozvezdie = dct['Mars']
print(dct)

planet_name = 'Mars'
planet_method = dct[planet_name]
planet_sozvezdie = planet_method(ephem.now())