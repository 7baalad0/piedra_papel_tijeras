import random

def eleccion_jugador() -> str:
    opcionjugador = input("Escoge Piedra, Papel o Tijeras: ").lower()
    return opcionjugador


def eleccion_maquina() -> str:
    random_maquina = random.randint(0,2)
    if random_maquina == 0:
        opcion_maquina = "piedra"
    if random_maquina == 1:
        opcion_maquina = "papel"
    if random_maquina == 2:
        opcion_maquina = "tijeras"
    return opcion_maquina


def partida():
    jugador = eleccion_jugador()
    maquina = eleccion_maquina()

    print("Jugador:", jugador," Máquina:", maquina) 

    if jugador == "piedra":
        if maquina == "piedra":
            return "Empate."
        elif maquina == "papel":
            return "Has perdido..."
        elif maquina == "tijeras":
            return "¡Tú ganas!"

    elif jugador == "papel":
        if maquina == "piedra":
            return "¡Tú ganas!"
        elif maquina == "papel":
            return "Empate."
        elif maquina == "tijeras":
            return "Has perdido..."

    elif jugador == "tijeras":
        if maquina == "piedra":
            return "Has perdido..."
        elif maquina == "papel":
            return "¡Tú ganas!"
        elif maquina == "tijeras":
            return "Empate."
    else:
        return "Escoge una opcion válida."

print(partida())
