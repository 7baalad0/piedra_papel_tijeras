import random
contador_jugador = 0
contador_maquina = 0
    
def eleccion_jugador() -> str:
    return input("Escoge Piedra, Papel o Tijeras: ").lower()
    
def eleccion_maquina(opcionjugador) -> str:
    
    if contador_jugador > contador_maquina:
        if opcionjugador == "piedra":
            return "papel"  
        elif opcionjugador == "papel":
            return "tijeras"  
        elif opcionjugador == "tijeras":
            return "piedra"  
    
    else:
        random_maquina = random.randint(0,2)
        if random_maquina == 0:
            return "piedra"
        elif random_maquina == 1:
            return "papel"
        elif random_maquina == 2:
            return "tijeras"

def partida(opcionjugador , maquina, contador_maquina, contador_jugador):
 
    print("Jugador:", opcionjugador ," Máquina:", maquina) 

    if opcionjugador == "piedra":
        if maquina == "piedra":
            resultado = "Empate."
        elif maquina == "papel":
            contador_maquina += 1
            resultado = "Has perdido..."
        elif maquina == "tijeras":
            contador_jugador += 1
            resultado = "¡Tú ganas!"
    elif opcionjugador == "papel":
        if maquina == "piedra":
            contador_jugador += 1
            resultado = "¡Tú ganas!"
        elif maquina == "papel":
            resultado = "Empate."
        elif maquina == "tijeras":
            contador_maquina +=1
            resultado = "Has perdido..."

    elif opcionjugador == "tijeras":
        if maquina == "piedra":
            contador_maquina +=1
            resultado = "Has perdido..."
        elif maquina == "papel":
            contador_jugador +=1
            resultado = "¡Tú ganas!"
        elif maquina == "tijeras":
            resultado = "Empate."
    else:
        resultado = "Escoge una opcion válida."
        
    return contador_maquina, contador_jugador, resultado

jugar = "s"
while jugar == "s": 

    while contador_jugador < 3 and contador_maquina < 3:
        opcionjugador = eleccion_jugador()
        maquina = eleccion_maquina(opcionjugador )
        contador_maquina, contador_jugador, resultado = partida(opcionjugador , maquina, contador_maquina, contador_jugador)
        print(resultado, "Jugador:", contador_jugador, "Máquina:", contador_maquina)
        
    if contador_jugador == 3:
        print("¡Que suerte, me has ganado!")
    elif contador_maquina == 3:
        print("Vaya, has perdido...")
    
    jugar_de_nuevo = ""
    while jugar_de_nuevo !="s" and jugar_de_nuevo !="n":
        jugar_de_nuevo = input("¿Quieres la revancha? (s/n): ").lower()
        if jugar_de_nuevo == "s":
            contador_jugador = 0
            contador_maquina = 0
            print ("Así me gusta. ¡Vamos allá!")
            break
        elif jugar_de_nuevo == "n":
            print("Bien jugado, ¡hasta la próxima!")
            jugar = "n"
            break
        else:
            print("No te he entendido. Introduce un valor correcto")
            