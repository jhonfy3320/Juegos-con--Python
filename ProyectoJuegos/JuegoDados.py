import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0

    def lanzar_dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        self.puntuacion = dado1 + dado2
        print(f"{self.nombre} lanzó {dado1} y {dado2}, sumando {self.puntuacion}")

def determinar_ganador(jugador1, jugador2):
    if jugador1.puntuacion > jugador2.puntuacion:
        print(f"{jugador1.nombre} gana con una puntuación de {jugador1.puntuacion}")
    elif jugador1.puntuacion < jugador2.puntuacion:
        print(f"{jugador2.nombre} gana con una puntuación de {jugador2.puntuacion}")
    else:
        print("Es un empate!")

def main():
    print("Bienvenidos al juego de dados!")
    
    nombre_jugador1 = input("Introduce el nombre del Jugador 1: ")
    nombre_jugador2 = input("Introduce el nombre del Jugador 2: ")
    
    jugador1 = Jugador(nombre_jugador1)
    jugador2 = Jugador(nombre_jugador2)
    
    jugador1.lanzar_dados()
    jugador2.lanzar_dados()
    
    determinar_ganador(jugador1, jugador2)

if __name__ == "__main__":
    main()
