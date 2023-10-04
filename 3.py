#Un conductor se encuentra en el kilómetro 18 de una carretera y otro 
#conductor se encuentra en el kilómetro 82 de dicha carretera, los coches 
#tienen sentido opuesto y tienen la misma velocidad. Realizar un programa 
#para determinar en qué kilómetro de esa carretera se encontrarán ambos 
#conductores.

kilometro_conductor1 = 18
kilometro_conductor2 = 82
velocidad = 45

kilometro_de_encuentro = (kilometro_conductor1 + kilometro_conductor2)/velocidad

print(f"Los conductores se encontraran en el kilometro {kilometro_de_encuentro}")

# kilometro_conductor1 = 18
# kilometro_conductor2 = 82
# velocidad_conductor1 = float(input("Ingrese la velocidad de conductor1 "))
# velocidad_conductor2 = float(input("Ingrese la velocidad de conductor2 "))

# kilometro_de_encuentro = (kilometro_conductor1 * velocidad_conductor2 + kilometro_conductor2 * velocidad_conductor1)/(velocidad_conductor1 + velocidad_conductor2)

# print(f"Los conductores se encontraran en el kilometro {kilometro_de_encuentro}")