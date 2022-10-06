from models.Nivel import Nivel

if __name__ == '__main__':
    jugadores=["Francisco","Joss"]
    # Se setean las escaleras y serpientes según la imágen del documento de requerimientos
    # Se usa un diccionario para indicar la posicion inicial y final
    escaleras={1:38,6:14,7:31,14:26,20:42,35:44,27:84,50:67,70:91,77:98,86:94}
    serpientes={98:80,94:75,91:88,88:68,73:53,63:60,61:19,45:25,48:11,15:6}
    nivel = Nivel(jugadores,escaleras,serpientes)
    nivel.iniciar()
