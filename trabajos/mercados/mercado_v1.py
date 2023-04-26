nombre = input("ingresar el nombre del producto: ") #string
stock = input("ingrese el stock del producto: ") #entero
precio = input("ingrese el precio del producto: ") #flotante
oferta = input("tiene oferta el producto? ") #booleano

#validar el nombre
if nombre == "":
    nombre = input("error, ingrese un nombre: ")
#validar el stoc
if stock == "":
    print("debe ingrear un valor")
else:
    stock = int(stock)
#validar el precio
if precio == "":
    print("debe ingrear un valor")
else:
    precio = float(precio)
#validar la oferta
if oferta == "si":
    porcentaje = precio*(5/100)
    total = precio - porcentaje
else:
    total = precio


print(f"hay {stock} unidades de {nombre} que valen {total} cada una.")
