#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de introducir una opción inválida, el programa informará de que no es correcta.

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
    print("3. Mostrar la multiplicación de los dos números")
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

# Función para realizar la suma de los dos números
def suma(num1, num2):
    return num1 + num2

# Función para realizar la resta de los dos números
def resta(num1, num2):
    return num1 - num2

# Función para realizar la multiplicación de los dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

opcion = mostrar_menu()

if opcion == '1':
    resultado = suma(num1, num2)
    print("La suma de", num1, "y", num2, "es:", resultado)
elif opcion == '2':
    resultado = resta(num1, num2)
    print("La resta de", num1, "y", num2, "es:", resultado)
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
    print("La multiplicación de", num1, "y", num2, "es:", resultado)
else:
    print("Opción inválida. Por favor, seleccione una opción válida (1, 2 o 3).")