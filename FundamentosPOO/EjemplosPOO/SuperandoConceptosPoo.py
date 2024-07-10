'''
Resumen y Explicación
Atributos y Métodos
Atributos: Son variables asociadas a una clase o a sus objetos que definen sus propiedades. Por ejemplo, una clase Persona podría tener atributos como nombre, edad y dirección.
Métodos: Son funciones definidas dentro de una clase que describen los comportamientos de los objetos de esa clase. Por ejemplo, en la clase Persona, podríamos tener métodos como hablar, caminar y comer.
Uso de super() en Python
La función super() permite acceder y llamar a métodos definidos en una superclase desde una subclase. Esto es útil para extender o modificar la funcionalidad de los métodos de la superclase sin repetir la implementación completa.

Jerarquía de Clases y Constructores
Cuando una clase hereda de otra, y esta a su vez hereda de otra clase, super() se utiliza para asegurar que todas las clases padre sean inicializadas correctamente.

Métodos que Vienen por Defecto en Python
Todas las clases en Python heredan de la clase base object, lo que proporciona ciertos métodos por defecto:

__init__(self): Constructor de la clase, se llama al crear una nueva instancia y se utiliza para inicializar atributos.
__str__(self): Devuelve una representación en cadena del objeto, usada por print() y str().
__repr__(self): Devuelve una representación “oficial” del objeto, usada por repr() y diseñada para ser precisa y útil para recrear el objeto.
Importancia de Aprender estos Conceptos
Extender Funcionalidades: super() permite extender funcionalidades de la superclase sin duplicar código.
Inicialización Correcta: El uso adecuado de constructores garantiza que todos los atributos sean inicializados correctamente.
Personalizar Representaciones: Métodos como __str__ y __repr__ permiten personalizar la representación de los objetos, facilitando la depuración y manejo de datos.
Comparar y Ordenar Objetos: Métodos como __eq__, __lt__, etc., permiten definir cómo se comparan y ordenan los objetos, esencial para muchas operaciones de datos.
'''
#Ejemplo de Atributos y Métodos
class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def hablar(self):
        print(f"{self.nombre} está hablando.")

    def caminar(self):
        print(f"{self.nombre} está caminando.")

# Crear una instancia de Persona
persona = Persona("Juan", 30, "Calle 123")
persona.hablar()  # Salida: Juan está hablando.
persona.caminar()  # Salida: Juan está caminando.

#Ejemplo de super()
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

# Crear una instancia de Perro
perro = Perro("Firulais", "Labrador")
print(perro.hacer_sonido())  # Salida: Guau

#Ejemplo de Jerarquía de Clases y Constructores

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

class Deportivo(Coche):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

# Crear una instancia de Deportivo
deportivo = Deportivo("Ferrari", "F8", 340)
print(deportivo.marca)  # Salida: Ferrari
print(deportivo.modelo)  # Salida: F8
print(deportivo.velocidad_maxima)  # Salida: 340

#Ejemplo de Métodos por Defecto
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

# Crear una instancia de Persona
persona = Persona("Ana", 28)
print(persona)  # Salida: Persona: Ana, Edad: 28
print(repr(persona))  # Salida: Persona('Ana', 28)

#Estos ejemplos te ayudarán a comprender mejor los conceptos avanzados de la 
#Programación Orientada a Objetos en Python y cómo aplicarlos en la práctica.