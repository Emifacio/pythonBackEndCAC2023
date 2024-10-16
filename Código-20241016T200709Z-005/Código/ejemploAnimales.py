#Superclase
class Animal():
    def __init__(self,nombre):
        self.nombre = nombre
    
    def dormir(self):
        print(f"{self.nombre} esta durmiendo.")
    
    def presentarse(self):
        print(f"Hola, soy un animalito y me llamo {self.nombre}")

    def hablar(self):
        print(f"Estoy hablando")
#-------------------------------------------------------
#Subclase
class Perro(Animal):
    def __init__(self, nombre,color):
        super().__init__(nombre)
        self.color = color
    
    def dar_patita(self):
        print("Soy un perro que da la patita!")
    
    def hablar(self):
        print("Guau guau guau!")

#Subclase
class Gato(Animal):
    def __init__(self, nombre,color):
        super().__init__(nombre)
        self.color = color
    
    def jugar_raton(self):
        print("Soy un gato que juega con el raton!")
    
    def hablar(self):
        print("Miau miau miau!")

toby = Perro("Toby","negro")
michi = Gato("Lola","blanco")

def expresar(x):
    x.hablar()

expresar(toby)
expresar(michi)