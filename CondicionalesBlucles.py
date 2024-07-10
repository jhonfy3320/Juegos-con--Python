# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bucle for con continue y break
for numero in numeros:
    if numero % 2 == 0:
        continue  # Saltar números pares
    if numero > 8:
        break  # Terminar el bucle si el número es mayor a 8
    print(f"Número impar: {numero}")

print("Bucle for completado")

# Bucle while con control de iteración
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Saltar números pares
    if contador > 8:
        break  # Terminar el bucle si el número es mayor a 8
    print(f"Número impar: {contador}")

print("Bucle while completado")

# Uso de pass en un bucle for
for numero in range(10):
    if numero % 2 == 0:
        pass  # Marcador de posición para futuros desarrollos
    else:
        print(f"Número impar (con pass): {numero}")

print("Bucle for con pass completado")
