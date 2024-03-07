#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
#'día', 'buen', 'Di'].

# 1.Definir la lista original
lista_original = ['Di', 'buen', 'día', 'a', 'papa']

# 2.Crear una nueva lista que sea la lista original invertida
lista_invertida = lista_original[::-1]

print(lista_invertida)