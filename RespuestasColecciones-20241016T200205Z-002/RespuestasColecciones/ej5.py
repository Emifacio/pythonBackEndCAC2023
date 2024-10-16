def promedio(notas):
    suma = 0
    for i in notas:
        suma += i
    return suma/len(notas)

def aprobaron(diccionario):
    aprobados = []
    for x,y in diccionario.items():
        if promedio(y) >= 8:
            aprobados.append(x)
    return aprobados

alumnos = {
    "juan": [7,7,7],
    "ana": [8,8,8,8],
    "hernando": [1],
    "blas":[8,9,10,6],
    "lucas":[4,5,3,6]
}

print(aprobaron(alumnos))

# Forma mas linda visualmente para mostrar el resultado:
# print("Los alumnos que aprobaron son ",end = "")
# for x in aprobaron(alumnos):
#     print(x,end=", ")
