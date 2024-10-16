def dni(numero):
    if len(numero) == 7 or len(numero) == 8:
        return True
    else:
        return False

elDNI = input("Ingrese su dni:") #Noten que trabajo con string para poder usar la funcion len()
if dni(elDNI):
    print("Es correcto.")
else:
    print("Esto no es un DNI")