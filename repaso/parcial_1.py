# Ejercicio 1
# Desarrollar un algoritmo que permita ingresar números enteros hasta que dicho número sea cero o un número negativo y mostrar:
#  a) La cantidad de números impares.
#  b) El promedio de números pares múltiplos de 4.

""" num1 = input("ingresar un numero: ")

while num1 == "":
    num1 = input("debe ingresar un numero para continuar: ")

num1 = int(num1)

while num1 > 0:
    print("el numero es positivo")
    break """
    
# Ejercicio 2
# Desarrollar un algoritmo que brinde información sobre el consumo de 20 clientes selectos de una empresa telefónica Para ello se ingresa, por cada uno de los clientes: 
# Nombre del Cliente- Duración de la llamada en minutos. -Tipo de abono: “A”, “B” o “C”.

# Para calcular el importe de cada llamada, nos informan que el costo por minuto, de acuerdo al tipo de abono, es el siguiente: 
# Abono “A” => $2 el minuto.
# Abono “B” => Los primeros 5 minutos a $2 el minuto. $1,5 el minuto adicional.
# Abono “C” => $1 el minuto con un máximo de $10 (Ej: si habla 15 minutos, paga $10).

# Al finalizar la carga, el algoritmo debe mostrar:
#     1. La recaudación total de la empresa.
#     2. La cantidad de clientes por cada tipo de abono.
#     3. El porcentaje de llamadas con duración superior a 5 minutos

nombre_cliente = input("ingresar el nombre del cliente: ")
duracion_llamada = input("ingresar el numero de minutos de la llamada: ")
tipo_abono = input("ingresar el tipo de abono [A/B/C]: ")

while nombre_cliente == "" or duracion_llamada =="" or tipo_abono == "":
    print("debe ingrear todos los valores para continuar")
    nombre_cliente = input("ingresar el nombre del cliente: ")
    duracion_llamada = input("ingresar el numero de minutos de la llamada: ")
    tipo_abono = input("ingresar el tipo de abono [A/B/C]: ")
    
duracion_llamada = int(duracion_llamada)

#calcular importe de la llamada.
if tipo_abono =="A":
    costo_llamada = 2 * duracion_llamada
elif tipo_abono =="B":
    if duracion_llamada < 5:
        costo_llamada = 2 * duracion_llamada
    else:
        excedente = duracion_llamada - 5
        costo_llamada = 10 + (excedente * 1.5)
else:
    if duracion_llamada < 10:
        costo_llamada = 1 * duracion_llamada
    else:
        costo_llamada = 10.0
        
        
print(f"El nombre del cliente es {nombre_cliente}, la duracion de la llamada fue de {duracion_llamada} minutos, su tipo de abono es {tipo_abono}, y el costo de la llamada es de ${costo_llamada}")
