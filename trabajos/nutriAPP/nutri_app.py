peso = int(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su altura en metros: "))
imc = peso / (altura**2)

if imc < 16:
    print(f"usted tiene delgadez severa, y su imc es: {imc}")
elif imc >= 16 and imc <= 16.99:
    print(f"usted tiene delgadez moderada y su imc es: {imc}")
elif imc >= 17 and imc <= 18.49:
    print(f"usted tiene delgadez leve y su imc es: {imc}")
elif imc >= 18.50 and imc <= 24.99:
    print(f"usted tiene peso normal, y su imc es: {imc}")
elif imc >= 25 and imc <= 29.99:
    print(f"usted tiene sobrepeso, y su imc es: {imc}")
elif imc >= 30 and imc <= 34.99:
    print(f"usted tiene obesidad de grado I, y su imc es: {imc}")
elif imc >= 35 and imc <= 39.99:
    print(f"usted tiene obesidad de grado II, y su imc es: {imc}")
else:
    print(f"usted tiene obesidad de grado III, y su imc es: {imc}")


