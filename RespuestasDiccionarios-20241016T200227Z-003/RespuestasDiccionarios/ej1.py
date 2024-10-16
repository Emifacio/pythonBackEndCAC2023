frutas = {
    "naranja": 180,
    "banana": 350,
    "manzana": 280,
    "pera": 300,
}
suma = 0
pedido = 0
while pedido != "n":
    pedido = input("Qué fruta quiere comprar? Si ingresa n termina.\n").lower()
    if pedido == "n":
        continue
    while pedido not in frutas.keys():
        pedido = input("No es correcto. Qué quiere comprar?\n").lower()
    kilos = int(input("Cuantos kilos quiere comprar?\n"))
    while kilos < 0:
        kilos = int(input("No es correcto. Cuantos kilos quiere comprar?\n"))
    suma += frutas[pedido] * kilos

print(f"Tiene que pagar ${suma}.")