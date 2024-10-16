
compras = {}
producto = 0
suma = 0
while producto != "n":
    producto = input("Que quiere comprar? Si ingresa n finaliza.")
    if producto == "n":
        continue
    precio = int(input("Cual es su precio?"))
    while precio < 0:
        precio = int(input("No es correcto. Cual es su precio?\n"))
    compras[producto] = precio
    suma += precio
print("-------------------------------")
for i,x in compras.items():
    print(i,x)
print("-------------------------------")
print(f"Tiene que pagar {suma}$")