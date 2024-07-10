Numbers = {1:'nicolas',
           2: 'emanuel',
           3:'alejandro',
           4:'kevin',
           5: 'sebastian',
           6: 'martin',
           7: 'freddy'}
print(Numbers)

Edades = {'nicolas': 13,
          'emanuel': 14,
          'alejandro': 12,
          'kevin': 7,
           'sebastian':7,
           'martin': 8,
            'freddy': 24, 
           'lases':12  }
print(Edades)
del Edades['lases']
print(Edades)
Claves = Edades.keys()
print(Claves)
print(type(Claves))

values = Edades.values()
print(values)
pairs = Edades.items()
print(pairs)


Edades2 = {'Nombres': {1:'nicolas',
           2: 'emanuel',
           3:'alejandro',
           4:'kevin',
           5: 'sebastian',
           6: 'martin',
           7: 'freddy'},
        'Edadess': {'nicolas': 13,
          'emanuel': 14,
          'alejandro': 12,
          'kevin': 7,
           'sebastian':7,
           'martin': 8,
            'freddy': 24, 
           'lases':12  }}

print(Edades2)
print(Edades2['Edadess'])


print('#'*100)
'''
Los diccionarios en Python son estructuras de datos muy poderosas que permiten almacenar pares de claves y valores. 
Son útiles cuando necesitas asociar datos relacionados y acceder a ellos de manera eficiente utilizando claves.

Conceptos Básicos sobre Diccionarios
Un diccionario en Python se crea utilizando llaves {} y contiene una colección no ordenada de pares clave: valor.

Creación de Diccionarios'''
# Crear diccionario
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Medellín"
}

# Acceder a valores
nombre = diccionario["nombre"]
edad = diccionario["edad"]
print("Nombre:", nombre)
print("Edad:", edad)

# Modificar valores
diccionario["edad"] = 31
print("Diccionario actualizado:", diccionario)

# Agregar nuevos pares
diccionario["ocupación"] = "Ingeniero"
print("Diccionario con nueva clave:", diccionario)

# Eliminar pares
del diccionario["ciudad"]
print("Diccionario después de eliminar 'ciudad':", diccionario)

# Verificar si una clave existe en el diccionario
print("¿'nombre' está en el diccionario?", "nombre" in diccionario)

# Obtener todas las claves
claves = diccionario.keys()
print("Claves:", list(claves))

# Obtener todos los valores
valores = diccionario.values()
print("Valores:", list(valores))

# Obtener todos los pares clave-valor
items = diccionario.items()
print("Pares clave-valor:", list(items))

'''
Usos de los Diccionarios en la Vida Real
Los diccionarios son extremadamente útiles en la vida real para diversas aplicaciones:

Almacenamiento de Datos Configurables: Se utilizan para almacenar configuraciones y parámetros en aplicaciones.'''

print('#'*100)
# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json
json_data = json.dumps(libro)
print("Datos en JSON:", json_data)
