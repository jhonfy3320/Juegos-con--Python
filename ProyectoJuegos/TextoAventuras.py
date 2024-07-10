class JuegoDeAventuras:
    def __init__(self):
        self.ubicacion_actual = 'entrada'
        self.ubicaciones = {
            'entrada': {
                'descripcion': 'Estás en la entrada de una cueva oscura.',
                'opciones': {'ir al norte': 'cueva'}
            },
            'cueva': {
                'descripcion': 'Estás dentro de la cueva. Hay un pasillo al norte y una salida al sur.',
                'opciones': {'ir al norte': 'sala de tesoros', 'ir al sur': 'entrada'}
            },
            'sala de tesoros': {
                'descripcion': 'Has encontrado la sala de tesoros. ¡Felicidades! Has ganado el juego.',
                'opciones': {}
            }
        }

    def mostrar_ubicacion(self):
        ubicacion = self.ubicaciones[self.ubicacion_actual]
        print(ubicacion['descripcion'])
        for opcion, destino in ubicacion['opciones'].items():
            print(f"- {opcion}")

    def tomar_decision(self, decision):
        if decision in self.ubicaciones[self.ubicacion_actual]['opciones']:
            self.ubicacion_actual = self.ubicaciones[self.ubicacion_actual]['opciones'][decision]
        else:
            print("Decisión no válida. Intenta nuevamente.")

    def jugar(self):
        while True:
            self.mostrar_ubicacion()
            if not self.ubicaciones[self.ubicacion_actual]['opciones']:
                break
            decision = input("¿Qué deseas hacer? ")
            self.tomar_decision(decision)
        print("Fin del juego.")

# Ejemplo de uso:
juego = JuegoDeAventuras()
juego.jugar()
