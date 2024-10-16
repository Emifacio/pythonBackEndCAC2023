#Superclase
class Persona():
    def __init__(self,nombre,anio_nacimiento):
        self.nombre = nombre
        self.nacimiento = anio_nacimiento
    def saludar(self):
        print(f"Hola {self.nombre}!")
    def comer(self):
        print("Estas comiendo.")
    def dormir(self):
        print("Te dormiste una siesta")

#SubClase
class Paciente(Persona):
    def __init__(self, nombre, anio_nacimiento, turno, obraSocial):
        # self.nombre = nombre
        # self.nacimiento = anio_nacimiento
        super().__init__(nombre,anio_nacimiento)
        self.turno = turno
        self.obraSocial = obraSocial
    def irAlTurno(self):
        print("Estas entrando a tu turno!")

class Medico(Persona):
    def __init__(self, nombre, anio_nacimiento, guardia, tarea):
        # self.nombre = nombre
        # self.nacimiento = anio_nacimiento
        super().__init__(nombre,anio_nacimiento)
        self.guardia = guardia
        self.tarea = tarea
    def operar(self):
        print("Estas operando a alguien!")

persona1 = Paciente("Jose",1987,5,"ObraSocial1")

persona1.comer()