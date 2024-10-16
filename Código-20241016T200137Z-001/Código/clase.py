# continuar = input("Quiere continuar? si/no").lower()
# if continuar == "si":
#     print("continuamos...")

# nombre = "Juan"
# edad = 34
# print("Su nombre es",nombre,"y su edad es",edad)
# print(f"Su nombre es {nombre} y su edad es {edad}")

# lista = ["hola",True,34,[3,6,"chau"],2]
# print(lista[3][2][2])

# notas = []
# for i in range(10):
#     numero = int(input("Que nota se saco? "))
#     while numero not in [0,1,2,3,4,5,6,7,8,9,10]:
#         numero = int(input("Valor incorrecto. Que nota se saco? "))
#     notas.append(numero)
# print(notas)

# lista = ["hamburguesa","cafe","gaseosa","cubanitos","papas fritas"]
# for i in range(len(lista)):
#     print(lista[i])

comidas = {
    "hamburguesa":700,
    "papas fritas":500,
    "gaseosa":400,
    "cafe":400,
}
for nombre,precio in comidas.items():
    if precio >= 500:
        print(f"La comida {nombre} sale {precio} pesos.")

alumnos = {
    4342333: {"nombre":"Ana","apellido":"Perez","notas":[7,6,8,7,6],"edad":18}
}

print(alumnos[4342333]["notas"][2])

