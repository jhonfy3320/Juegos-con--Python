import random

class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = 1
        self.experiencia = 0

    def atacar(self, enemigo):
        daño = self.ataque - enemigo.defensa
        if daño > 0:
            enemigo.salud -= daño
            print(f"{self.nombre} inflige {daño} puntos de daño a {enemigo.nombre}.")
        else:
            print(f"{self.nombre} no puede penetrar la defensa de {enemigo.nombre}.")

    def esta_vivo(self):
        return self.salud > 0

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            self.ataque += 5
            self.defensa += 5
            self.salud += 20
            print(f"{self.nombre} ha subido al nivel {self.nivel}.")

class JuegoRPG:
    def __init__(self):
        self.jugador = Personaje("Héroe", 100, 20, 10)
        self.enemigos = [
            Personaje("Goblin", 50, 10, 5),
            Personaje("Orco", 80, 15, 10),
            Personaje("Dragón", 200, 25, 20)
        ]

    def combate(self, enemigo):
        print(f"¡Un {enemigo.nombre} salvaje ha aparecido!")
        while self.jugador.esta_vivo() and enemigo.esta_vivo():
            self.jugador.atacar(enemigo)
            if enemigo.esta_vivo():
                enemigo.atacar(self.jugador)
        if self.jugador.esta_vivo():
            print(f"¡{self.jugador.nombre} ha derrotado a {enemigo.nombre}!")
            self.jugador.ganar_experiencia(50)
        else:
            print(f"{self.jugador.nombre} ha sido derrotado. Fin del juego.")

    def jugar(self):
        while self.jugador.esta_vivo() and self.enemigos:
            enemigo = random.choice(self.enemigos)
            self.combate(enemigo)
            self.enemigos.remove(enemigo)
        if self.jugador.esta_vivo():
            print("¡Todos los enemigos han sido derrotados! ¡Has ganado el juego!")

# Ejemplo de uso:
juego_rpg = JuegoRPG()
juego_rpg.jugar()

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego Simple con Pygame")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Posición del cuadrado
x, y = 400, 300
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(30)
