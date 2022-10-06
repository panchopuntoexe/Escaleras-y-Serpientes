import random as rd


class Dado:
    """
    Clase que gestiona los lanzamientos del dado

    Métodos
    -------
    lanzar()
        Simula el lanzamiento de un dado de 6 lados
    """

    def lanzar(self):
        return rd.randint(1, 6)
