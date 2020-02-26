import ephem # модуль для определения в каком созвездии находится планета на определенную дату

planets = {'Mars': ephem.Mars, 'Mercury': ephem.Mercury, 'Venus': ephem.Venus, 'Jupiter': ephem.Jupiter, 'Saturn': ephem.Saturn,
       'Uranus': ephem.Uranus, 'Neptune': ephem.Neptune, 'Pluto': ephem.Pluto, 'Sun': ephem.Sun, 'Moon': ephem.Moon
       }

planet_name = 'Venus' # подставить сюда из сообщения пользователя
planet_method = planets[planet_name] # из словаря по ключу 'Venus' - ephem.Venus
planet_constellation = planet_method(ephem.now()) # к 'Ven
print(planet_constellation)
