class Persona:
    def __init__(self,cedula,nombre,apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self) -> str:
        return f"({self.cedula}) {self.apellido} {self.nombre}"
    
class Destreza:
    def __init__(self,area,herramienta,experiencia):
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia
    def __str__(self):
        return f"{self.area} {self.herramienta} {self.experiencia}"

#-----------------------------------------------------
#Clase que hereda de Persona y Destreza
class Jefe(Persona,Destreza):
    def __init__(self, cedula, nombre, apellido,area,herramienta,experiencia,grupoJefe):
        Persona.__init__(self,cedula, nombre, apellido)
        Destreza.__init__(self,area,herramienta,experiencia)
        self.grupo = grupoJefe
    def __str__(self):
        return(f"Se llama {self.nombre} {self.apellido}, area {self.area} con la herramienta {self.herramienta}, su experiencia es {self.experiencia} y pertenece al grupo {self.grupo}")

print("-"*30)
persona1 = Persona(123456789,"Juan","Perez")
print(persona1)
print("-"*30)

destreza1 = Destreza("Programacion","Python","Experto")
print(destreza1)
print("-"*30)

jefe1 = Jefe(423123321,"Ana","Jaurez","Diseño","Interfaz","alta",1)
print(jefe1)
print("-"*30)

