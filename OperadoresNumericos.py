A = 20 
B = 6

print('suma: ', A + B)
print('resta: ', A - B)
print('Multiplicacion: ' , A * B)
print('Division: ', A / B)

# OPeraciones en programación 
print('Modulo: ', A & B)
print('Parte entera de la divisison: ', A // B)
print('Potenciación: ', A ** B)

# Shortcus Atajos
print('##'*50)
A  += 10
A  -= 10
A  *= 10
A  /= 10
print(A)

#Regla pendas Reglas matematicas de opraciones que serian 
'''
Potenciación,
Exponenciación,
Matematicas,
División,
Addición,
Sustración'''
print('##'*50)
Operaciones_1 = 2 + 6 * 6 / 6 - 8
Operaciones_2 = (24 * 78) + 24 


print(Operaciones_1)
print(Operaciones_2)

Operaciones_3 = (20 +120 * (13 ** 12) / 16 - 5)
print(Operaciones_3)

#Operadores Booleanos
print(A > B)
print(A < B)
print(A >= B)
print(A <= B)


print('*' * 100)
# Operadores Aritméticos
a = 5
b = 3

print("Operadores Aritméticos")
print(f"Suma: {a} + {b} = {a + b}")       # Salida: 8
print(f"Resta: {a} - {b} = {a - b}")      # Salida: 2
print(f"Multiplicación: {a} * {b} = {a * b}")  # Salida: 15
print(f"División: {a} / {b} = {a / b}")   # Salida: 1.6666666666666667
print(f"División Entera: {a} // {b} = {a // b}")  # Salida: 1
print(f"Módulo: {a} % {b} = {a % b}")     # Salida: 2
print(f"Potencia: {a} ** {b} = {a ** b}") # Salida: 125

print("\nOperadores de Comparación")
print(f"Igual: {a} == {b} -> {a == b}")   # Salida: False
print(f"Distinto: {a} != {b} -> {a != b}")# Salida: True
print(f"Mayor que: {a} > {b} -> {a > b}") # Salida: True
print(f"Menor que: {a} < {b} -> {a < b}") # Salida: False
print(f"Mayor o igual que: {a} >= {b} -> {a >= b}") # Salida: True
print(f"Menor o igual que: {a} <= {b} -> {a <= b}") # Salida: False

print("\nOperadores Lógicos")
print(f"and: {a} > {b} and {a} > 0 -> {a > b and a > 0}")   # Salida: True
print(f"or: {a} > {b} or {a} < 0 -> {a > b or a < 0}")      # Salida: True
print(f"not: not({a} > {b}) -> {not(a > b)}")              # Salida: False

print("\nOperadores de Asignación")
c = 10
print(f"Asignación: c = {c}")                              # Salida: 10
c += 5
print(f"Asignación de suma: c += 5 -> c = {c}")            # Salida: 15
c -= 3
print(f"Asignación de resta: c -= 3 -> c = {c}")           # Salida: 12
c *= 2
print(f"Asignación de multiplicación: c *= 2 -> c = {c}")  # Salida: 24
c /= 4
print(f"Asignación de división: c /= 4 -> c = {c}")        # Salida: 6.0
c %= 3
print(f"Asignación de módulo: c %= 3 -> c = {c}")          # Salida: 0.0
c = 10
c //= 2
print(f"Asignación de división entera: c //= 2 -> c = {c}") # Salida: 5
c **= 3
print(f"Asignación de potencia: c **= 3 -> c = {c}")       # Salida: 125

print("\nOperadores Bit a Bit")
print(f"AND: {a} & {b} -> {a & b}")    # Salida: 1
print(f"OR: {a} | {b} -> {a | b}")     # Salida: 7
print(f"XOR: {a} ^ {b} -> {a ^ b}")    # Salida: 6
print(f"NOT: ~{a} -> {~a}")            # Salida: -6
print(f"Desplazamiento a la izquierda: {a} << 1 -> {a << 1}") # Salida: 10
print(f"Desplazamiento a la derecha: {a} >> 1 -> {a >> 1}")   # Salida: 2
