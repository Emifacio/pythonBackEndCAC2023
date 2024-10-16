def promedio(notas):
    suma = 0
    for i in notas:
        suma += i
    return suma/len(notas)

notasJuan = [4,8,6,7,9]
print(f"El promedio del alumno es {promedio(notasJuan)}")