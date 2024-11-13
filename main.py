import random
from typing import Union, Tuple
contador_jugador:int = 0
contador_maquina:int = 0
maquina_tramposa:bool = False

def frase_ganar() -> str:  #Frases aleatorias para cuando ganas la partida
    if contador_jugador == 3 and contador_maquina == 0:   #Frase especial para el 3 - 0
        return "Menuda paliza histórica me acabas de meter. Mi enhorabuena"
    frase = ["Esta vez ganas. Pura potra", "Esa no me la esperaba. Tú ganas", "Ganaste. Aunque me estaba dejando, échate una revancha y verás"]
    return random.choice(frase)

def frase_perder() -> str:  #Frases aleatorias para cuando pierdes la partida
    if contador_maquina == 3 and contador_jugador == 0: #Frase especial para el 0 - 3
        return "Vaya, perder así es incluso mas díficil que ganar. Siéntete orgulloso"
    frase = ["Has perdido. Muy predecible todo.", "Pierdes... ¿De verdad pensabas que no me la venía venir?", "Perdiste. Necesito un rival decente..."]
    return random.choice(frase)
    
def eleccion_jugador() -> str:   #Elección del jugador
    return input("Escoge Piedra, Papel o Tijeras: ").lower()
    
def eleccion_maquina(opcionjugador) -> Union [str,int]:  #Elección de la máquina
    
    if maquina_tramposa and contador_jugador > contador_maquina:  #Si la maquina tramposa fue activada y se cumplen las condiciones hará trampas
        if opcionjugador == "piedra":
            return "papel"  
        elif opcionjugador == "papel":
            return "tijeras"  
        elif opcionjugador == "tijeras":
            return "piedra"  
    
    else:                                          #En cualquier otro caso escogerá una opción aleatoria
        random_maquina = random.randint(0,2)  
        if random_maquina == 0:
            return "piedra"
        elif random_maquina == 1:
            return "papel"
        elif random_maquina == 2:
            return "tijeras"

def partida(opcionjugador:str, maquina:Union[str,int], contador_maquina:int, contador_jugador:int) -> Tuple [int,int,str]: #Funcion que define las reglas de la partida y quién gana cada ronda
 
    print("Jugador:", opcionjugador ," Máquina:", maquina)  #Enseña que sacó el jugador y la máquina en la ronda

    if opcionjugador == "piedra": 
        if maquina == "piedra":
            resultado = "Empate."
        elif maquina == "papel":
            contador_maquina += 1
            resultado = "Has perdido la ronda."
        elif maquina == "tijeras":
            contador_jugador += 1
            resultado = "¡Ganas esta ronda!"
    elif opcionjugador == "papel":
        if maquina == "piedra":
            contador_jugador += 1
            resultado = "¡Ganas esta ronda!"
        elif maquina == "papel":
            resultado = "Empate."
        elif maquina == "tijeras":
            contador_maquina +=1
            resultado = "Has perdido la ronda."

    elif opcionjugador == "tijeras":
        if maquina == "piedra":
            contador_maquina +=1
            resultado = "Has perdido la ronda."
        elif maquina == "papel":
            contador_jugador +=1
            resultado = "¡Ganas esta ronda!"
        elif maquina == "tijeras":
            resultado = "Empate."
    else:
        resultado = "Escoge una opcion válida."
        
    return contador_maquina, contador_jugador, resultado

jugar:str = "s"     
while jugar == "s":  #Bucle principal del juego, llama al resto de funciones y hace que las rondas mientras no se llegue a 3 y las partidas vuelvan a empezar mientras quieras
    
    activar_trampa:str = ""
    while activar_trampa !="s" and activar_trampa !="n":      #Bucle para activar o desactivar la máquina tramposa
        activar_trampa = input("¿Quieres activar la máquina tramposa? (s/n): ").lower()
        if activar_trampa == "s":
            maquina_tramposa = True
            print("Máquina tramposa activada.")
            break
        elif activar_trampa == "n":
            print("Se ha desactivado la máquina tramposa.")
            break
        else:
            print("Introduce un valor correcto")

    while contador_jugador < 3 and contador_maquina < 3:    #Bucle que hace que se jueguen rondas hasta que alguien llegue a 3 puntos
        opcionjugador = eleccion_jugador()
        maquina = eleccion_maquina(opcionjugador )
        contador_maquina, contador_jugador, resultado = partida(opcionjugador , maquina, contador_maquina, contador_jugador)
        print(resultado, "Jugador:", contador_jugador, "Máquina:", contador_maquina)
        
    if contador_jugador == 3:     #Finaliza la partida diciendo el ganador con las frases aleatorias
        print(frase_ganar())
    elif contador_maquina == 3:
        print(frase_perder())
    
    jugar_de_nuevo = ""                                                  
    while jugar_de_nuevo !="s" and jugar_de_nuevo !="n":                    #Pregunta al final de cada partida si se quiere volver a jugar. Si no, el programa finalizará.
        jugar_de_nuevo = input("¿Quieres la revancha? ;) (s/n): ").lower()
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
            