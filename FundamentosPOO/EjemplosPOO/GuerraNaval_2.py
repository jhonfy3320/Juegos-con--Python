import random

class Barco:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
        self.posiciones = []
        self.hundido = False

    def colocar(self, posiciones):
        self.posiciones = posiciones

    def recibir_disparo(self, posicion):
        if posicion in self.posiciones:
            self.posiciones.remove(posicion)
            if not self.posiciones:
                self.hundido = True
            return True
        return False

class Tablero:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tablero = [['~'] * tamaño for _ in range(tamaño)]
        self.barcos = []

    def colocar_barco(self, barco, posiciones):
        for x, y in posiciones:
            self.tablero[x][y] = 'B'
        barco.colocar(posiciones)
        self.barcos.append(barco)

    def disparar(self, x, y):
        for barco in self.barcos:
            if barco.recibir_disparo((x, y)):
                self.tablero[x][y] = 'X'
                if barco.hundido:
                    print(f"¡Hundiste el {barco.nombre}!")
                else:
                    print(f"¡Tocado!")
                return True
        self.tablero[x][y] = 'O'
        print("¡Agua!")
        return False

    def mostrar(self):
        for fila in self.tablero:
            print(" ".join(fila))

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero_propio = Tablero()
        self.tablero_oponente = Tablero()

    def colocar_barco(self, barco, posiciones):
        self.tablero_propio.colocar_barco(barco, posiciones)

    def disparar(self, oponente, x, y):
        return oponente.tablero_propio.disparar(x, y)

class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = jugador1

    def jugar(self):
        while True:
            print(f"Turno de {self.turno_actual.nombre}")
            self.turno_actual.tablero_oponente.mostrar()
            x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
            if self.turno_actual == self.jugador1:
                if self.turno_actual.disparar(self.jugador2, x, y):
                    if self.jugador2.tablero_propio.barcos == []:
                        print(f"¡{self.jugador1.nombre} ha ganado!")
                        break
                self.turno_actual = self.jugador2
            else:
                if self.turno_actual.disparar(self.jugador1, x, y):
                    if self.jugador1.tablero_propio.barcos == []:
                        print(f"¡{self.jugador2.nombre} ha ganado!")
                        break
                self.turno_actual = self.jugador1

# Ejemplo de uso:
# Crear jugadores
jugador1 = Jugador("Jugador 1")
jugador2 = Jugador("Jugador 2")

# Crear y colocar barcos
barco1 = Barco("Acorazado", 4)
barco2 = Barco("Submarino", 3)
barco3 = Barco("Destructor", 2)

jugador1.colocar_barco(barco1, [(1, 1), (1, 2), (1, 3), (1, 4)])
jugador1.colocar_barco(barco2, [(3, 3), (3, 4), (3, 5)])
jugador1.colocar_barco(barco3, [(5, 5), (5, 6)])

jugador2.colocar_barco(barco1, [(2, 2), (2, 3), (2, 4), (2, 5)])
jugador2.colocar_barco(barco2, [(4, 4), (4, 5), (4, 6)])
jugador2.colocar_barco(barco3, [(6, 6), (6, 7)])

# Iniciar el juego
juego = Juego(jugador1, jugador2)
juego.jugar()
