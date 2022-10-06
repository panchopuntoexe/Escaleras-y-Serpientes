from models.Dado import Dado
from models.Token import Token


class Jugador:
    """
    Clase que comprueba los movimientos del jugador y verifica que sean legales 

    Atributos
    ----------
    nombre : str
        Nombre del jugador
    tablero : list
        Lista de casillas
    dado : Dado
        Dado usado en el juego
    token : Token
        Token del jugador

    Métodos
    -------
    iniciar_movimiento()
        Mueve al token del jugador según la lógica de escaleras y serpientes
    __str__
        Imprime una cadena de texto con el nombre y a posición del jugador
    """

    def __init__(self, nombre,tablero):
        self.nombre = nombre
        self.tablero = tablero
        self.dado = Dado()
        self.token = Token()

    #Gestiona el movimiento, retorna false si sigue jugando y true si ganó el juego
    def iniciar_movimiento(self) -> bool:
        movimientos=self.dado.lanzar()
        posicion_nueva=self.token.posicionActual+movimientos

        print("Se lanzó el dado: " + str(movimientos))
        #Cambia la posición del token solo si es menor o igual a la 100
        if posicion_nueva<=100:
            #Obtiene la posición nueva consultando si la casilla es serpiente, escalera o normal
            movimiento_extra = self.tablero.casillas[posicion_nueva-1].verificar_movimiento_extra()
            self.token.moverse(movimientos+movimiento_extra)

            print("Nueva posición de "+self.__str__())
        return posicion_nueva==100
    
    def __str__(self) -> str:
        return self.nombre+" en la posición " +self.token.__str__()