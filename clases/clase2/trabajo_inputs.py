#trabajando con inputs
n = int(input("ingresa un numero: "))
if n < 100:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")
#---------------------------
clima = input("ingresar como esta el clima: ")
if clima == "Hoy esta lloviendo":
    print("hay que tomarse el colectivo")
else:
    print("vamos caminando") 
#---------------------------
peso = int(input("ingresar tu peso: "))
if peso < 78:
    print("tener que comer")
elif peso == 78:
    print("estas en el peso justo")
else:
    print("cortame los postres")
#---------------------------
dia = input("que dia es? ")
mi_condicion = input("cual es tu condicion? ")

if dia == "sabado":
    print("hoy se sale furte")
elif dia == "domingo":
    if mi_condicion == "jaqueca":
        print("recobrarse, luego descansar")
    else:
        print("descansar")
else:
    print("trabajar")
