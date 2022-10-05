import random as rd

class Partida:
    
    def __init__(self, jugadores, tablero):
        self.jugadores = jugadores
        self.tablero = tablero

    def iniciar_juego(self):
        bandera=False
        while(not bandera):
            for jugador in self.jugadores:
                print("\n***** Turno de "+jugador.__str__()+" *****")
                bandera=jugador.iniciar_movimiento()
                if(bandera):
                    break
        


class Dado:
    
    def lanzar(self):
        return rd.randint(1,6)

class Token:
    
    def __init__(self):
        self.posicionActual=1

    def moverse(self,posicion_nueva):
        self.posicionActual=posicion_nueva
        
    def __str__(self) -> str:
        return str(self.posicionActual)

class ControladorDeMovimiento:
    
    def __init__(self, tablero):
        self.tablero = tablero

    def verificar_movimiento_extra(self,posiciones_a_moverse):
        self.posicionActual+=posiciones_a_moverse
        return 


class Jugador:

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
        #Cambia la posición del token solo si es menor o igual a 100
        if posicion_nueva<=100:
            #Obtiene la posición nueva consultando si el casillero es serpiente, escalera o normal
            posicion_nueva = self.tablero.casilleros[posicion_nueva-1].verificarMovimientoExtra()
            self.token.moverse(posicion_nueva)
            print("Nueva posición de "+self.__str__())
        return posicion_nueva==100
    
    def __str__(self) -> str:
        return self.nombre+" en la posición " +self.token.__str__()

class Casillero:
    
    def __init__(self, posicion):
        self.posicion = posicion
        self.posicion_final = posicion

    def set_posicion_final(self, posicion_final):
        self.posicion_final = posicion_final

    def verificarMovimientoExtra(self):
        if self.posicion==self.posicion_final:
            return self.posicion
        else:
            print("Se añadió un movimiento extra")
            return self.posicion_final

class Tablero:
    
    def __init__(self, casilleros):
        self.casilleros = casilleros


class Nivel:
    def __init__(self):
        casilleros = []
        for posicion in range(100):
            casilleros.append(Casillero(posicion+1))

        #Escaleras
        casilleros[1].set_posicion_final(38)
        casilleros[6].set_posicion_final(14)
        casilleros[7].set_posicion_final(31)
        casilleros[14].set_posicion_final(26)
        casilleros[20].set_posicion_final(42)
        casilleros[35].set_posicion_final(44)
        casilleros[27].set_posicion_final(84)
        casilleros[50].set_posicion_final(67)
        casilleros[70].set_posicion_final(91)
        casilleros[77].set_posicion_final(98)
        casilleros[86].set_posicion_final(94)

        #Serpientes
        casilleros[98].set_posicion_final(80)
        casilleros[94].set_posicion_final(75)
        casilleros[91].set_posicion_final(88)
        casilleros[88].set_posicion_final(68)
        casilleros[73].set_posicion_final(53)
        casilleros[63].set_posicion_final(60)
        casilleros[61].set_posicion_final(19)
        casilleros[45].set_posicion_final(25)
        casilleros[48].set_posicion_final(11)
        casilleros[15].set_posicion_final(6)

        tablero=Tablero(casilleros)
        jugadores = [Jugador("Francisco",tablero),Jugador("David",tablero),Jugador("Joss",tablero)]
        partida = Partida(jugadores,tablero)
        partida.iniciar_juego()

if __name__ == '__main__':
    Nivel()
    
