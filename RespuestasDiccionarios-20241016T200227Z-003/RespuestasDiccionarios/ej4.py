datos = {}
alumno = 1
salir = False
while not salir:
    opcion = input('''Ingrese una opción:
    1: Agregar alumno.
    2: Eliminar el alumno que yo desee (por nombre)
    3. Darme el apellido de un alumno. 
    4. Editar la edad de un alumno. 
    5. Finalizar. 
    ''')
    if opcion == "1":
        alumno = input("Ingrese el nombre del alumno:\n")
        apellido = input(f"Ingrese el apellido de {alumno}\n")
        edad = int(input(f"Ingrese la edad de {alumno}\n"))
        while edad < 12:
            edad = int(input(f"No es valido. Ingrese la edad de {alumno}\n"))
        datos[alumno] = [apellido,edad]
    elif opcion == "2":
        alumno = input("Ingrese el nombre del alumno que quiere eliminar:\n")
        if alumno in datos.keys():
            datos.pop(alumno)
        else:
            print("El alumno no existe.")
    elif opcion == "3":
        alumno = input("Ingrese el nombre del alumno y le dire el apellido:\n")
        if alumno in datos.keys():
            print(f"El apellido de {alumno} es {datos[alumno][0]}")
        else:
            print("El alumno no existe.")
    elif opcion == "4":
        alumno = input("Ingrese el nombre del alumno:\n")
        if alumno in datos.keys():
            edad = int(input(f"Ingrese la edad nueva de {alumno}:\n"))
            while edad < 12:
                edad = int(input(f"No es valido. Ingrese la edad nueva de {alumno}:\n"))
            datos[alumno][1] = edad
        else:
            print("El alumno no existe.")
    elif opcion == "5":
        salir = True
    else:
        print("No es una opcion valida.")
print("La lista de alumnos es la siguiente:")
for x,i in datos.items():
    print(f"El alumno {x} {i[0]} tiene {i[1]} años")