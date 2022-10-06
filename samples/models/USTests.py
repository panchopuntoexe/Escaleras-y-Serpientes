from io import StringIO
import unittest

from models.Nivel import Nivel

class US1(unittest.TestCase):
    """
    Given the game is started
    When the token is placed on the board
    Then the token is on square 1
    """

    def test_UAT1(self):
        nivel = Nivel()
        # nivel.iniciar()
        self.assertEqual(nivel.jugadores[0].token.get_posicion_actual(), 1)

    """
    Given the token is on square 1
    When the token is moved 3 spaces
    Then the token is on square 4
    """

    def test_UAT2(self):
        nivel = Nivel()
        nivel.jugadores[0].token.moverse(3)
        self.assertEqual(nivel.jugadores[0].token.get_posicion_actual(), 4)

    """
    Given the token is on square 1
    When the token is moved 3 spaces
    And then it is moved 4 spaces
    Then the token is on square 8
    """

    def test_UAT3(self):
        nivel = Nivel()
        nivel.jugadores[0].token.moverse(3)
        nivel.jugadores[0].token.moverse(4)
        self.assertEqual(nivel.jugadores[0].token.get_posicion_actual(), 8)


class US2(unittest.TestCase):
    """
    Given the token is on square 97
    When the token is moved 3 spaces
    Then the token is on square 100
    And the player has won the game
    """

    def test_UAT1(self):
        nivel = Nivel()
        # nivel.iniciar()
        nivel.jugadores[0].token.posicionActual = 97
        nivel.jugadores[0].token.moverse(3)
        self.assertEqual(nivel.jugadores[0].token.get_posicion_actual(), 100)

    """
    Given the token is on square 97
    When the token is moved 4 spaces
    Then the token is on square 97
    And the player has not won the game
    """

    def test_UAT2(self):
        nivel = Nivel()
        nivel.jugadores[0].token.posicionActual = 97
        nivel.jugadores[0].token.moverse(4)
        self.assertEqual(nivel.jugadores[0].token.get_posicion_actual(), 97)


class US3(unittest.TestCase):
    """
    Given the game is started
    When the player rolls a die
    Then the result should be between 1-6 inclusive
    """

    def test_UAT1(self):
        nivel = Nivel()
        # nivel.iniciar()
        resultado_de_lanzamiento = nivel.jugadores[0].dado.lanzar()
        self.assertGreaterEqual(resultado_de_lanzamiento, 1)
        self.assertLessEqual(resultado_de_lanzamiento, 6)

    """
    Given the player rolls a 4
    When they move their token
    Then the token should move 4 spaces
    """

    def test_UAT2(self):
        nivel = Nivel()
        posicion_inicial = nivel.jugadores[0].token.get_posicion_actual()

        resultado_de_lanzamiento = nivel.jugadores[0].dado.lanzar()
        while (resultado_de_lanzamiento != 4):
            resultado_de_lanzamiento = nivel.jugadores[0].dado.lanzar()

        nivel.jugadores[0].token.moverse(resultado_de_lanzamiento)
        
        posicion_final = nivel.jugadores[0].token.get_posicion_actual()
        self.assertEqual(posicion_final - posicion_inicial, 4)

class Tests:
    def __init__(self) -> None:
        from pprint import pprint
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream)
        result = runner.run(unittest.makeSuite(US1))
        result = runner.run(unittest.makeSuite(US2))
        result = runner.run(unittest.makeSuite(US3))
        print ('Tests run ', result.testsRun)
        print ('Errors ', result.errors)
        pprint(result.failures)
        stream.seek(0)
        print (stream.read())