#Generando Funciones 
from audioop import add

from numpy import subtract


def greet():
    print('Hola a todos como estan NEAKSMFYPY')

greet()

#Almacenando valores en las funciones 
def greet(name, last_name):
    print('Hola a todos como estan NEAKSMFYPY', name, last_name)


greet('nico', 'Osorio')
greet('emanuel', 'Ososrio')
greet('alejandro', 'Vivas')
greet('kevin', 'Ososrio')
greet('sebastian', 'Osorio')
greet('martin', 'ososrio')
greet('freddy', 'Tavera')

#Almacenando valores en las funciones 
def greet(name, last_name = 'No tiene apellido'):
    print('Hola a todos como estan NEAKSMFYPY', name, last_name)


greet('nico', 'Osorio')
greet('emanuel', 'Ososrio')
greet('alejandro', 'Vivas')
greet('kevin')
greet('sebastian', 'Osorio')
greet('martin', 'Ososrio')
greet('freddy', 'Tavera')

#Almacenando valores en las funciones 
def greet(name, last_name = 'No tiene apellido'):
    print('Hola a todos como estan NEAKSMFYPY', name, last_name)


# greet(name= 'nico', last_name= 'Osorio')
greet('emanuel', 'Ososrio')
greet('alejandro', 'Vivas')
greet('kevin')
greet('sebastian', 'Osorio')
greet('martin', 'Ososrio')
greet('freddy', 'Tavera')
greet(name= 'nico', last_name= 'Osorio')


print('#'*100)
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_area_circulo(radio, pi=3.14159):
    """Calcula el área de un círculo."""
    return pi * radio ** 2

# Llamadas a las funciones
area_rectangulo = calcular_area_rectangulo(5, 3)
area_circulo = calcular_area_circulo(2)

print(f"Área del rectángulo: {area_rectangulo}")  # Salida: Área del rectángulo: 15
print(f"Área del círculo: {area_circulo}")  # Salida: Área del círculo: 12.56636
