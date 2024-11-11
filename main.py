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

print (eleccion_maquina())