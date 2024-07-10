#Definición de una Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
juan = Persona("Jhon Freddy", 30)
juan.saludar()  # Salida: Hola, mi nombre es Juan y tengo 30 años.


# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)
        self.universidad = universidad

    def estudiar(self):
        print(f"{self.nombre} está estudiando en {self.universidad}.")

#Crear un Objeto de la Clase Derivada
ana = Estudiante("Ana", 22, "MIT")
ana.saludar()        # Salida: Hola, mi nombre es Ana y tengo 22 años.
ana.estudiar()       # Salida: Ana está estudiando en MIT.
