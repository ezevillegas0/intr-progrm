#Un  algoritmo  es  una  secuencia  ordenada  y  finita  de  pasos  tal  que  su  ejecución  resuelve  un determinado problema o n grupo de problemas. 

#Una variable es una posición de memoria donde se puede almacenar un valor. Las variables pueden ser de tipo entero (int), real (float), cadena de caracteres (string) o booleano (bool).

#primer ejercicio
""" base = int(input("ingrese la medida de la base: "))
altura = int(input("ingrese la medida de la altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"el perimetro del rectangulo es : {perimetro}")
print(f"el area del rectangulo es: {area}") """

# * Multiplicación r = 2 * 6  # r es 12 
# ** Exponente r = 2 ** 6  # r es 64 
# / División r = 3.5 / 2  # r es 1.75 
# // División entera r = 3.5 // 2  # r es 1.0 
# % Módulo (resto de la división entera) r = 7 % 2  # r es 1 

#segundo ejercicio if y while
""" nro = input("ingrese un numero: ")
while nro == "":
    nro = input("debe ingresar un numero para continuar: ")

nro = int(nro)
if nro < 0:
    print("el numero es negativo")
elif nro > 0:
    print("el numero es positivo")
else:
    print("el numero es 0") """
    
# not Negación (no) 
# and Conjunción (y) 
# or Disyunción (o)

#tercer ejercicio
nro = input("ingrese un numero: ")
while nro == "":
    nro = input("debe ingresar un numero para continuar: ")
nro = int(nro)
if nro >= 10 and nro <= 100:
    print("el numero teiene dos cifras")
else:
    print("el numero no tiene dos cifras")