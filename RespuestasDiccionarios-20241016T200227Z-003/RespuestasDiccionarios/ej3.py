datos = {}
alumno = 1
while alumno != "n":
    alumno = input("Ingrese el nombre del alumno, si ingresa n termina:\n")
    if alumno == "n":
        continue
    apellido = input(f"Ingrese el apellido de {alumno} \n")
    edad = int(input(f"Ingrese la edad de {alumno}\n"))
    while edad < 12:
        edad = int(input(f"No es valido. Ingrese la edad de {alumno}\n"))
    datos[alumno] = (apellido,edad)
alumno = input("Ingrese el nombre del alumno del cual quiere saber la información:\n")
print(f"{alumno} {datos[alumno][0]} tiene {datos[alumno][1]} años.")
