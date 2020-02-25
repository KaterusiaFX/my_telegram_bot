import ephem # модуль для определения в каком созвездии находится планета на определенную дату

mars = ephem.Mars('2000/01/01') # определяет где находится Mars по дате 2000/01/01
print(mars)

const = ephem.constellation(mars) # определяет созвездие для переменной mars (constellation - это атрибут модуля ephem)
print(const)
