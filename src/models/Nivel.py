from models.Jugador import Jugador
from models.Tablero import Tablero
from models.Casilla import Casilla
from models.Partida import Partida


class Nivel:
    """
    Clase que inicializa el la partida con dos jugadores y una estructura específica de escaleras y serpientes
    """

    def __init__(self,nombres_de_jugadores,escaleras,serpientes):
        self.nombres_de_jugadores = nombres_de_jugadores
        self.escaleras = escaleras
        self.serpientes = serpientes
        casillas = self.crear_tablero_personalizado()
        self.tablero = Tablero(casillas)

    def iniciar(self):
        partida = Partida(self.nombres_de_jugadores,self.tablero)
        # Inicializo la partida
        partida.iniciar_juego()

    def crear_tablero_personalizado(self):
        casillas = []

        #Creación de todas las casillas
        for posicion in range(100):
            casillas.append(Casilla(posicion+1))

        #Seteo de las escaleras y serpientes
        for posicion in self.escaleras:
            casillas[posicion].set_posicion_final(self.escaleras[posicion])
        for posicion in self.serpientes:
            casillas[posicion].set_posicion_final(self.serpientes[posicion])

        return casillas
