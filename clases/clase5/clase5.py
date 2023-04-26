#clase 5 - bucles

#primer while

""" i = 0 

while i < 100:
    print("hola")
    i += 1
print("el contador llego a su final") """
#segundo while

nombre = input("ingrese el nombre: ")

while nombre == "":
    nombre = input("error debe ingresar el nombre: ")

print(f"hola {nombre}, como te va?")
#tercer while

dni = input("ingrese su dni: ")

while len(dni)<7 and len(dni)>8:
    dni = input("error, reingrese su dni")
print(f"tu dni es {dni}")