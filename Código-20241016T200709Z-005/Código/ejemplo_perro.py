class Perro:
    # Atributo de Clase
    genero= "Canis"
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    # Método de instancia

    @property #De esta forma puedo acceder al valor de __nombre
    def consultar_nombre(self):
        return self.__nombre
    
    @consultar_nombre.setter
    def consultar_nombre(self,edad):
        if edad <= 20:
            self.__nombre = edad
            print("Se cambio la edad correctamente!")
        else:
            print(f"Error, la edad {edad} no es posible")

    def imprimir(self):
        return f'{self.__nombre} tiene {self.edad} años.'
    # Otro método de instancia
    def ladrar(self, sonido):
        return f'{self.__nombre} dice {sonido}.'

    # Se puede reemplazar el método imprimir() con __str__()
    def __str__(self):
        return f'{self.__nombre} tiene {self.edad} años.'

miMascota = Perro("Lola", 11)
miMascota.imprimir()
miMascota.ladrar("Guau guau!")
# print(miMascota.__nombre)
miMascota.consultar_nombre = 26
miMascota.consultar_nombre




