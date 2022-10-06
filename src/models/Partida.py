class Partida:
    """
    Clase que gestiona los turnos de jugadores y el fin del juego.
    El juego finaliza cuando uno de los jugadores llega al final del tablero

    Atributos
    ----------
    jugadores : list
        lista de jugadores

    Métodos
    -------
    iniciar_juego()
        Comienza el juego con los jugadores en el tablero
    """

    def __init__(self, jugadores):
        self.jugadores = jugadores

    # Itera sobre la lista de jugadores
    def iniciar_juego(self):
        bandera = False
        while (not bandera):
            for jugador in self.jugadores:
                print("\n***** Turno de "+jugador.__str__()+" *****")

                # Comentar la siguiente línea si se quiere mostrar todo el juego sin interrupciones
                input("Presiona enter para lanzar el dado ")
                bandera = jugador.iniciar_movimiento()

                # Verifico que hubo algún ganador para finalizar la partida
                if (bandera):
                    break
