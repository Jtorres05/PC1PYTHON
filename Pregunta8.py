# 1.Solicitar al usuario la hora en formato HH:MM
hora = input("Ingrese la hora en formato HH:MM: ")

# 2.Dividir la hora en horas y minutos
horas, minutos = map(int, hora.split(':'))

# 3.Determinar si es hora de desayuno, almuerzo o cena
if 7 <= horas < 8 and 0 <= minutos < 60:
    print("Es hora de desayunar.")
elif 12 <= horas < 13 and 0 <= minutos < 60:
    print("Es hora de almorzar.")
elif 18 <= horas < 19 and 0 <= minutos < 60:
    print("Es hora de cenar.")