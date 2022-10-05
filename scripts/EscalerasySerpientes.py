import random as rd


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

    #Itera sobre la lista de jugadores
    def iniciar_juego(self):
        bandera=False
        while(not bandera):
            for jugador in self.jugadores:
                print("\n***** Turno de "+jugador.__str__()+" *****")
                
                #Comentar la siguiente línea si se quiere mostrar todo el juego sin interrupciones
                input("Presiona enter para lanzar el dado ")
                bandera=jugador.iniciar_movimiento()
                if(bandera):
                    break
        
class Dado:
    """
    Clase que gestiona los lanzamientos del dado

    Métodos
    -------
    lanzar()
        Simula el lanzamiento de un dado de 6 lados
    """
    
    def lanzar(self):
        return rd.randint(1,6)

class Token:
    """
    Clase que mantiene la posición del token de un jugador. 

    Atributos
    ----------
    posicionActual : int
        posición en el tablero de 1 a 100

    Métodos
    -------
    lanzar()
        Simula el lanzamiento de un dado de 6 lados
    """
    
    def __init__(self):
        self.posicionActual=1

    def moverse(self,posicion_nueva):
        self.posicionActual=posicion_nueva
        
    def __str__(self) -> str:
        return str(self.posicionActual)

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
            posicion_nueva = self.tablero.casillas[posicion_nueva-1].verificarMovimientoExtra()
            self.token.moverse(posicion_nueva)

            print("Nueva posición de "+self.__str__())
        return posicion_nueva==100
    
    def __str__(self) -> str:
        return self.nombre+" en la posición " +self.token.__str__()

class Casilla:
    """
    Clase que abstrae el comportamiento de una casilla, ya sea de serpiente o escalera

    Atributos
    ----------
    posicion : int
        Posición asignada a la casilla, de 1 a 100
    posicion_final : int
        Si la casilla es inicio de una escalera o cabeza de serpiente, entonces tendrá un valor distinto al atributo posicion
    Métodos
    -------
    verificarMovimientoExtra
        Valida si la casilla es escalera, serpiente o normal
    """
    
    def __init__(self, posicion):
        self.posicion = posicion
        self.posicion_final = posicion

    def set_posicion_final(self, posicion_final):
        self.posicion_final = posicion_final

    #Función que retorna la posición final si la casilla no es normal
    def verificarMovimientoExtra(self):
        #Si la posicion y posicion_final son iguales entonces no se realiza ningún movimiento adicional
        if self.posicion==self.posicion_final:
            return self.posicion
        else:
            #Se indica que hubo algún tipo de penalización o premio
            print("Se añadió un movimiento extra")
            return self.posicion_final

class Tablero:
    """
    Clase contiene una lista de casillas

    Atributos
    ----------
    casillas : List
        Lista de casillas
    """
    
    def __init__(self, casillas):
        self.casillas = casillas

class Nivel:
    """
    Clase que inicializa el la partida con dos jugadores y una estructura específica de escaleras y serpientes
    """
    def __init__(self):
        casillas = []
        for posicion in range(100):
            casillas.append(Casilla(posicion+1))

        #Se setean las escaleras y serpientes según la imágen del documento de requerimientos
        #Escaleras
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

        #Serpientes
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

        tablero=Tablero(casillas)
        jugadores = [Jugador("Francisco",tablero),Jugador("David",tablero)]
        partida = Partida(jugadores)
        #Inicializo la partida
        partida.iniciar_juego()

if __name__ == '__main__':
    Nivel()