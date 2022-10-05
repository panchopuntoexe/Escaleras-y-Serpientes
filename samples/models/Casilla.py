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