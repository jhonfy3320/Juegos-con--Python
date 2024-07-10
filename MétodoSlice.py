A = [1,23,45,67,8,21,9, 'Nico',11,34,'freddy']
B = A
print(A)
print(B)
del A[0]
print(A)
print(B)
print(id(A))
print(id(B))
C = A[:]
print(C)
print(id(A))
print(id(B))
print(id(C))
A.append(12)
print(A)
print(B)
print(C)

'''El método slice en Python es una técnica muy útil para obtener una subsección de una lista 
(o de cualquier secuencia como cadenas de texto o tuplas). 
Permite seleccionar un rango específico de elementos utilizando la notación de corte (slicing).

Conceptos Básicos de Slicing
La sintaxis básica para el slicing es:

lista[inicio:fin:paso]
inicio: El índice de inicio del corte (incluido).
fin: El índice de fin del corte (excluido).
paso: El intervalo entre los índices seleccionados (opcional).
Si omites alguno de los parámetros, se utilizan los valores predeterminados:

inicio: 0 si se omite.
fin: Longitud de la lista si se omite.
paso: 1 si se omite.'''

print('#'*100)
# Ejemplos de Slicing
# Ejemplos de slicing en listas
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener una subsección de la lista
sublista1 = lista[2:5]       # Del índice 2 al 4 (5 excluido)
sublista2 = lista[:4]        # Desde el inicio hasta el índice 3 (4 excluido)
sublista3 = lista[5:]        # Desde el índice 5 hasta el final
sublista4 = lista[::2]       # Todos los elementos con paso de 2
sublista5 = lista[1:7:2]     # Del índice 1 al 6 (7 excluido) con paso de 2

# Slicing con índices negativos
sublista6 = lista[-5:]       # Últimos 5 elementos
sublista7 = lista[:-5]       # Todos menos los últimos 5
sublista8 = lista[-8:-2:2]   # Desde el índice -8 al -3 (excluido) con paso de 2

print("Lista original:", lista)
print("Sublista del índice 2 al 4:", sublista1)
print("Sublista desde el inicio al índice 3:", sublista2)
print("Sublista desde el índice 5 al final:", sublista3)
print("Sublista con paso de 2:", sublista4)
print("Sublista del índice 1 al 6 con paso de 2:", sublista5)
print("Últimos 5 elementos:", sublista6)
print("Todos menos los últimos 5:", sublista7)
print("Sublista del índice -8 al -3 con paso de 2:", sublista8)

print('#'*100)
# Ejemplo Completo con Slicing
# Aquí tienes un script completo que muestra varios usos del método slice:
# Lista de ejemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplos de slicing
sublista1 = lista[2:5]
sublista2 = lista[:4]
sublista3 = lista[5:]
sublista4 = lista[::2]
sublista5 = lista[1:7:2]

# Slicing con índices negativos
sublista6 = lista[-5:]
sublista7 = lista[:-5]
sublista8 = lista[-8:-2:2]

# Salida de resultados
print("Lista original:", lista)
print("Sublista del índice 2 al 4:", sublista1)
print("Sublista desde el inicio al índice 3:", sublista2)
print("Sublista desde el índice 5 al final:", sublista3)
print("Sublista con paso de 2:", sublista4)
print("Sublista del índice 1 al 6 con paso de 2:", sublista5)
print("Últimos 5 elementos:", sublista6)
print("Todos menos los últimos 5:", sublista7)
print("Sublista del índice -8 al -3 con paso de 2:", sublista8)
