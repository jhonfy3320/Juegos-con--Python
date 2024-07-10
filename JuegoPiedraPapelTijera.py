import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

# Bucle principal del juego
while True:
    # Elección del usuario
    usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    if usuario == "salir":
        break
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

'''
Explicación del Código
Importación de Módulos: random se utiliza para seleccionar aleatoriamente la elección de la computadora.
Definición de Opciones: Se define una lista de opciones disponibles para el juego.
Función determinar_ganador: Esta función compara las elecciones del usuario y la computadora 
para determinar el resultado del juego.
Bucle Principal del Juego:
Solicita al usuario que ingrese su elección.
Si el usuario ingresa "salir", el juego termina.
Si el usuario ingresa una opción no válida, se le pide que intente de nuevo.
La computadora elige una opción aleatoriamente.
Se determina y se muestra el resultado del juego.
Este juego sencillo te permitirá practicar la lógica condicional, el uso de bucles y 
la interacción con el usuario en Python. 
'''
