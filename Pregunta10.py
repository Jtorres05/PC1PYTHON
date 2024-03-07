#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']

# 1.Definir la lista original
lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# 2.Crear una nueva lista excluyendo los elementos en las posiciones 0, 4 y 5
nueva_lista = [lista_original[i] for i in range(len(lista_original)) if i not in [0, 4, 5]]

print(nueva_lista)