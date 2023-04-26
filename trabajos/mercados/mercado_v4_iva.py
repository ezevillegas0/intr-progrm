#trabajo mercado con while

#definiendo variables.
nombre = input("ingrese el nombre del producto: ")
stock = input("ingrese el stock del producto: ")
precio = input("ingrese el precio de producto: ")
oferta = input("el producto tiene oferta? ")
cantidad = input("cual es la cantidad deseada del producto: ")

while nombre == "":
    nombre = input("debe ingresar el nombre del producto para continuar: ")
    
while stock == "":
    stock = input("debe ingreasar el stock del procucto: ")

while precio =="":
    precio = input("debe ingresar el precio del producto: ")

#convirtiendo las variables.
stock = int(stock)
precio = float(precio)
cantidad = int(cantidad)
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

precio_iva = (total * 1.21)

if cantidad >= 10 and cantidad < 15:
    descuento = (2 * total) / 100
    precio_final = total - descuento
elif cantidad >= 15 and cantidad < 20:
    descuento = (3 * total) / 100
    precio_final = total - descuento
elif cantidad >= 20 and cantidad < 25:
    descuento = (4 * total) / 100
    precio_final = total - descuento
elif cantidad >= 25:
    descuento = (5 * total) / 100
    precio_final = total - descuento
else:
    precio_final = total
    
    
print(f"hay {stock} unidades de {nombre} que valen {total} cada una.")

print(f"precio con el iva : {precio_iva}")

print(f"el precio final es de: {precio_final}")