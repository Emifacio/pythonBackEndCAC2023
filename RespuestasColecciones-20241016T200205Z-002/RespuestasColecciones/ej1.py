def descuento(precio,porcentaje):
    return precio*(porcentaje/100)

producto = int(input("Ingrese el precio del producto:\n"))
promo = int(input("Ingrese el descuento:\n"))
print(descuento(producto,promo))