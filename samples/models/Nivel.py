from models.Jugador import Jugador
from models.Tablero import Tablero
from models.Casilla import Casilla
from models.Partida import Partida


class Nivel:
    """
    Clase que inicializa el la partida con dos jugadores y una estructura específica de escaleras y serpientes
    """

    def __init__(self):
        casillas = self.crear_tablero_personalizado()
        tablero = Tablero(casillas)
        self.jugadores = [Jugador("Francisco", tablero),
                          Jugador("David", tablero)]

    def iniciar(self):
        partida = Partida(self.jugadores)
        # Inicializo la partida
        partida.iniciar_juego()

    def crear_tablero_personalizado(self):
        casillas = []
        for posicion in range(100):
            casillas.append(Casilla(posicion+1))

        # Se setean las escaleras y serpientes según la imágen del documento de requerimientos
        # Escaleras
        casillas[1].set_posicion_final(38)
        casillas[6].set_posicion_final(14)
        casillas[7].set_posicion_final(31)
        casillas[14].set_posicion_final(26)
        casillas[20].set_posicion_final(42)
        casillas[35].set_posicion_final(44)
        casillas[27].set_posicion_final(84)
        casillas[50].set_posicion_final(67)
        casillas[70].set_posicion_final(91)
        casillas[77].set_posicion_final(98)
        casillas[86].set_posicion_final(94)

        # Serpientes
        casillas[98].set_posicion_final(80)
        casillas[94].set_posicion_final(75)
        casillas[91].set_posicion_final(88)
        casillas[88].set_posicion_final(68)
        casillas[73].set_posicion_final(53)
        casillas[63].set_posicion_final(60)
        casillas[61].set_posicion_final(19)
        casillas[45].set_posicion_final(25)
        casillas[48].set_posicion_final(11)
        casillas[15].set_posicion_final(6)

        return casillas
