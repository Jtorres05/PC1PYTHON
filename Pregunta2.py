#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

# 1. Solicitar al usuario el monto del consumo en el restaurante
consumo = float(input("¿Cuánto fue su consumo en el restaurante? $"))

# 2. Solicitar al usuario el porcentaje de propina deseado
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? "))

# 3. Calcular la cantidad de dinero a dejar como propina
propina = consumo * (porcentaje_propina / 100)

print("La cantidad de dinero a dejar como propina es: $",propina)