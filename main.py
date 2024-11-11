def eleccion_jugador() -> str:
    opcionjugador = input("Escoge Piedra, Papel o Tijeras: ").lower()
    return opcionjugador

print(eleccion_jugador())