def correo(texto):
    for i in texto:
        if i == "@":
            return True
    return False

cadena = input("Ingrese su correo:\n")
if correo(cadena):
    print("Es correcto.")
else:
    print("No es un correo valido.")

# Este ejercicio se puede mejorar para ser mas efectivos al analizar si es o no un correo electronico