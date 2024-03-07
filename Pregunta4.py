#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:1+2+3+...+n = (n*(n+1)/2)


# Solicitar al usuario que ingrese un entero positivo
N = int(input("Ingrese un entero positivo: "))

# Verificar si el número ingresado es positivo
if N <= 0:
    print("El número ingresado no es positivo.")
else:
    # Calcular la suma de los primeros N enteros positivos
    suma = N * (N + 1) // 2

    # Mostrar la suma de los primeros N enteros positivos
    print("La suma de los primeros", N, "enteros positivos es:", suma)