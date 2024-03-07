#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

# 1.Solicitar al usuario la edad del cliente
edad_cliente = int(input("Ingrese la edad del cliente: "))

# 2.Calcular el precio de la entrada según la edad del cliente
if edad_cliente < 4:
    precio_entrada = 0
elif edad_cliente >= 4 and edad_cliente <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar el precio de la entrada al cliente
print("El precio de la entrada es: $", precio_entrada)