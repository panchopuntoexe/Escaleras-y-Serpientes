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

    def moverse(self,movimientos):
        posicion_nueva=self.posicionActual+movimientos
        if posicion_nueva<=100:
            self.posicionActual=posicion_nueva
        
    def __str__(self) -> str:
        return str(self.posicionActual)