#trabajo mercado con while

#definiendo variables.
nombre = input("ingrese el nombre del producto: ")
stock = input("ingrese el stock del producto: ")
precio = input("ingrese el precio de producto: ")
oferta = input("el producto tiene oferta? ")

while nombre == "":
    nombre = input("debe ingresar el nombre del producto para continuar: ")
    
while stock == "":
    stock = input("debe ingreasar el stock del procucto: ")

while precio =="":
    precio = input("debe ingresar el precio del producto: ")

#convirtiendo las variables.
stock = int(stock)
precio = float(precio)
total = precio

if oferta == "si":
    oferta = True
elif oferta == "no":
    oferta = False
else:
    oferta = input("debe ingresar si el producto tiene oferta: ")

if oferta == True:
    porcentaje = (precio)*5/ 100
    #descuento = precioFinal * 0.05
    total = precio - porcentaje
    
print(f"hay {stock} unidades de {nombre} que valen {total} cada una.")