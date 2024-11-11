import random
contador_jugador = 0
contador_maquina = 0
    
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
    global contador_jugador, contador_maquina
    jugador = eleccion_jugador()
    maquina = eleccion_maquina()

    print("Jugador:", jugador," Máquina:", maquina)  

    if jugador == "piedra":
        if maquina == "piedra":
            return "Empate."
        elif maquina == "papel":
            contador_maquina = contador_maquina + 1
            return "Has perdido..."
        elif maquina == "tijeras":
            contador_jugador = contador_jugador + 1
            return "¡Tú ganas!"
    elif jugador == "papel":
        if maquina == "piedra":
            contador_jugador = contador_jugador + 1
            return "¡Tú ganas!"
        elif maquina == "papel":
            return "Empate."
        elif maquina == "tijeras":
            contador_maquina = contador_maquina + 1
            return "Has perdido..."

    elif jugador == "tijeras":
        if maquina == "piedra":
            contador_maquina = contador_maquina + 1
            return "Has perdido..."
        elif maquina == "papel":
            contador_jugador = contador_jugador + 1
            return "¡Tú ganas!"
        elif maquina == "tijeras":
            return "Empate."
    else:
        return "Escoge una opcion válida."

print(partida(), "Jugador :", contador_jugador, "Maquina:", contador_maquina)
