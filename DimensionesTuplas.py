Matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
print(Matrix)
print(Matrix[1][2])

#Generando tuplas 
Numbers = (1,2,3,4,5,6,7,8,910,11,12,13,14,15,16,17,18,19,20)
print(Numbers)
print(type(Numbers))
print(Numbers[0:4])
#las Tuplas no se pueden modificar son inmutables 
# Numbers[1] = 'Freddy'
# print(Numbers)

Numbers2 = 1,2,3,4,5,6,7,8,910,11,12,13,14,15,16,17,18,19,20
print(Numbers2)
#para generar las listas podemos usar parantesis o no usrlos 


print('#'*100)
'''
Listas de Múltiples Dimensiones
Las listas de múltiples dimensiones son listas que contienen otras listas como elementos. 
Una lista de dos dimensiones se asemeja a una matriz, donde cada elemento es una lista que representa una fila.'''

# Lista de dos dimensiones
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

print('#'*100)
# Lista de tres dimensiones
tensor = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("\nTensor:")
for bloque in tensor:
    for fila in bloque:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    print()


'''
Tuplas
Las tuplas son similares a las listas, pero son inmutables, lo que significa que no pueden ser modificadas después de su creación. 
Las tuplas se utilizan para almacenar colecciones de elementos heterogéneos y se crean utilizando paréntesis ().'''

print('#'*100)
# Tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print("Tupla1:", tupla1)
print("Tupla2:", tupla2)

tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

tupla_repetida = tupla1 * 2
print("Tupla repetida:", tupla_repetida)

print("¿Está 3 en la tupla1?", 3 in tupla1)
print("Longitud de tupla1:", len(tupla1))

print("Elementos de tupla1:")
for elemento in tupla1:
    print(elemento)

a, b, c = tupla1
print("Desempaquetado de tupla1:", a, b, c)

'''
Explicación del Código
Listas de Dos Dimensiones: Se crea una lista que representa una matriz, se accede a sus elementos y se iteran.
Listas de Tres Dimensiones: Se crea una lista que representa un tensor, se accede a sus elementos y se iteran.
Tuplas: Se crean tuplas, se accede a sus elementos, se muestran ejemplos de concatenación, repetición, verificación de 
pertenencia, longitud y desempaquetado.
Este script te proporciona una visión completa de cómo trabajar con listas de múltiples dimensiones y tuplas en Python. '''

print('#'*100)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Iterar e imprimir cada elemento:
for row in matrix:
    for element in row:
        print(element)