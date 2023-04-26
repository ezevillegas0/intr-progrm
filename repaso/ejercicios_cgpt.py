""" 1) ejercicios varios """

# Escribir un programa que lea un número entero y muestre por pantalla si es par o impar.

""" numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.") """

# Escribir un programa que lea dos números enteros y muestre por pantalla su suma, resta, multiplicación y división.

""" num1 = input("ingresar un numero: ")
num2 = input("ingresar otro numero: ")

num1 = int(num1)
num2 = int(num2)

suma = num1 + num2
print(f"la suma es de {suma}")
resta = num1 - num2
print(f"la resta es de {resta}")
multiplicacion = num1 * num2
print(f"la multiplicacion es de {multiplicacion}")
division = num1 / num2
print(f"la division es de {division}") """

# Escribir un programa que pida la base y la altura de un recatangulo y calcular sus medidas.

""" base = int(input("ingrese la medida de la base: "))
altura = int(input("ingrese la medida de la altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"el perimetro del rectangulo es : {perimetro}")
print(f"el area del rectangulo es: {area}") """ 

#final de ejercicios varios

""" 2) ejercicios if/elif/else """

# Escribir un programa que lea tres números enteros y muestre por pantalla el mayor de ellos.

""" num1 = input("ingresar un numero: ")
num2 = input("ingresar otro numero: ")
num3 = input("ingresar otro numero: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 or num1 > num3:
    print(f"el numero mayor es {num1}")
elif num2 > num1 or num2 > num3:
    print(f"el numero mayor es {num2}")
else:
    print(f"el numero mayor es {num3}") """

# Escribir un programa que lea el nombre y la edad de una persona y muestre por pantalla si es mayor de edad o no.

# Escribir un programa que lea una nota de un examen (un valor entre 0 y 10) y muestre por pantalla la calificación correspondiente: A si la nota es mayor o igual a 9, B si la nota es mayor o igual a 7, C si la nota es mayor o igual a 5, y F si la nota es menor a 5.

""" nota_examen = input("ingresar la nota del examen: ")
nota_examen = int(nota_examen)

if nota_examen >= 9:
    print("tenes una calificacion de A.")
elif nota_examen >= 7:
    print("tenes una calificacion de B.")
else:
    print("sos un burro") """

# Escribir un programa que lea un número entero y muestre por pantalla si es positivo, negativo o cero.

""" num1 = input("ingresar un numero: ")
num1 = int(num1)

if num1 == 0:
    print("el numero es cero.")
elif num1 > 0:
    print("el numero es positivo")
else:
    print("el numero es negativo.") """

# Escribir un programa que lea un número entero entre 1 y 7 y muestre por pantalla el día de la semana correspondiente, considerando que el lunes es el día 1.

# Escribir un programa que lea dos números enteros y muestre por pantalla el mayor de ellos, o un mensaje indicando que ambos son iguales.

# Escribir un programa que lea un número entero y muestre por pantalla si es un número primo o no.

""" ejercicios while """

#Escribir un programa que lea un número entero y muestre por pantalla todos los números enteros desde 1 hasta ese número.

""" num = int(input("Ingrese un número entero: "))
i = 1

while i <= num:
    print(i)
    i += 1 """

#Escribir un programa que lea números enteros hasta que se introduzca un número negativo y muestre por pantalla la suma de todos los números introducidos.

""" suma = 0

while True:
    num = int(input("Ingrese un número entero: "))
    if num < 0:
        break
    suma += num

print(f"La suma de todos los números ingresados es {suma}") """

#Escribir un programa que lea números enteros hasta que se introduzca un número negativo y muestre por pantalla la media de todos los números introducidos.

""" suma = 0
contador = 0

while True:
    num = int(input("Ingrese un número entero: "))
    if num < 0:
        break
    suma += num
    contador += 1

if contador == 0:
    print("No se ingresaron números positivos.")
else:
    media = suma / contador
    print("La media de todos los números ingresados es:", media) """