is_member = True
age = 15

#Un condicional dentro de otro condicional 
if is_member:
    if age >= 15:
        print('Tienes acceso ya que eres mayor o igual a 15 años ')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')


is_member = False
age = 15

#Un condicional dentro de otro condicional 
if is_member:
    if age >= 15:
        print('Tienes acceso ya que eres mayor o igual a 15 años ')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')


is_member = True
age = 11

#Un condicional dentro de otro condicional 
if is_member:
    if age >= 15:
        print('Tienes acceso ya que eres mayor o igual a 15 años ')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')


'''Las estructuras condicionales en Python son fundamentales para controlar el flujo de ejecución de un programa. 
Permiten ejecutar diferentes bloques de código en función de ciertas condiciones.

Conceptos Básicos de las Estructuras Condicionales
Las estructuras condicionales en Python incluyen if, elif y else. A continuación, te explico cómo funcionan y te doy algunos ejemplos.'''

# Condicional simple
edad = 20
if edad >= 18:
    print("Eres mayor de edad")

# Condicional con if y else
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Condicional con if, elif y else
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
else:
    print("Necesitas mejorar")

# Condicionales anidadas
nota = 85
edad = 20
if nota >= 70:
    if edad >= 18:
        print("Aprobado y mayor de edad")
    else:
        print("Aprobado pero menor de edad")
else:
    print("No aprobado")

# Validación de datos
entrada = input("Introduce tu edad: ")
if entrada.isdigit():
    edad = int(entrada)
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Por favor, introduce un número válido")

# Control de flujo en aplicaciones
opcion = input("Elige una opción (1, 2, 3): ")
if opcion == "1":
    print("Opción 1 seleccionada")
elif opcion == "2":
    print("Opción 2 seleccionada")
elif opcion == "3":
    print("Opción 3 seleccionada")
else:
    print("Opción no válida")
