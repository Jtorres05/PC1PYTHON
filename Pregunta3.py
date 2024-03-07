#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.

# 1.Definir el peso de cada payaso y muñeca en gramos
peso_payaso = 112
peso_muñeca = 75

# 2.Solicitar al usuario el número de payasos vendidos en el último pedido
payasos_vendidos = int(input("Ingrese el número de payasos vendidos en el último pedido: "))

# 3.Solicitar al usuario el número de muñecas vendidas en el último pedido
muñecas_vendidas = int(input("Ingrese el número de muñecas vendidas en el último pedido: "))

# 4.Calcular el peso total del paquete sumando el peso de los payasos y muñecas vendidos
peso_total_paquete = (peso_payaso * payasos_vendidos) + (peso_muñeca * muñecas_vendidas)

print("El peso total del paquete que será enviado es:", peso_total_paquete, "gramos")