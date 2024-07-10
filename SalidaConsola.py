#Iput
Name = input('Ingresa tu numbre: ')
print(Name)
print(type(Name))

Age = int(input('Ingresa tu edad: ')) #Entero
print(Age)
print(type(Age))

Age2 = float(input('Ingresa tu edad desimal: ')) #Entero
print(Age)
print(type(Age2))

print('//'*23)
# Operaciones de Entrada/Salida en Consola

# Entrada de datos
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? "))

# Salida de datos
print("\nDatos ingresados:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")

# Realizar algunas operaciones y mostrar resultados
a = int(input("\nIngresa un número entero para a: "))
b = int(input("Ingresa otro número entero para b: "))

print("\nOperaciones Aritméticas")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División Entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

print("\nOperadores de Comparación")
print(f"Igual: {a} == {b} -> {a == b}")
print(f"Distinto: {a} != {b} -> {a != b}")
print(f"Mayor que: {a} > {b} -> {a > b}")
print(f"Menor que: {a} < {b} -> {a < b}")
print(f"Mayor o igual que: {a} >= {b} -> {a >= b}")
print(f"Menor o igual que: {a} <= {b} -> {a <= b}")

print("\nOperadores Lógicos")
print(f"and: {a} > {b} and {a} > 0 -> {a > b and a > 0}")
print(f"or: {a} > {b} or {a} < 0 -> {a > b or a < 0}")
print(f"not: not({a} > {b}) -> {not(a > b)}")

print("\nOperadores de Asignación")
c = 10
print(f"Asignación: c = {c}")
c += 5
print(f"Asignación de suma: c += 5 -> c = {c}")
c -= 3
print(f"Asignación de resta: c -= 3 -> c = {c}")
c *= 2
print(f"Asignación de multiplicación: c *= 2 -> c = {c}")
c /= 4
print(f"Asignación de división: c /= 4 -> c = {c}")
c %= 3
print(f"Asignación de módulo: c %= 3 -> c = {c}")
c = 10
c //= 2
print(f"Asignación de división entera: c //= 2 -> c = {c}")
c **= 3
print(f"Asignación de potencia: c **= 3 -> c = {c}")

print("\nOperadores Bit a Bit")
print(f"AND: {a} & {b} -> {a & b}")
print(f"OR: {a} | {b} -> {a | b}")
print(f"XOR: {a} ^ {b} -> {a ^ b}")
print(f"NOT: ~{a} -> {~a}")
print(f"Desplazamiento a la izquierda: {a} << 1 -> {a << 1}")
print(f"Desplazamiento a la derecha: {a} >> 1 -> {a >> 1}")

# Salida final
print("\nGracias por utilizar el programa. ¡Hasta la próxima!")
