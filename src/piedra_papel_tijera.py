'''
NAME
    piedra_papel_tijera

VERSION
    1.0

AUTHOR
    Natalia Gutierrez Ponce

GITHUB
    https://github.com/natgupo19/python_class

DESCRIPTION
    Juego "piedra, papel o tijera" entre computadora y jugadora. La jugadora puede elegir 
    cualquiera de las tres opciones disponibles, la computadora elegira aleatoriamente. 

CATEGORY
    Game

USAGE
    py .\src\piedra_papel_tijera.py

ARGUMENTS
    None

INPUT
    Nombre del usuario.
    Eleccion del usuario entre "piedra", "papel" o "tijera".

OUTPUT
    Opciones elegidas y el resultado del juego.

SEE ALSO
    None
'''

# Importar libreria random
import random

# Dar la bienvenida y pedir nombre al usuario
print("\n¡Bienvenidx al juego de piedra, papel o tijera!\n")
name = input("Introduce tu nombre:\n")

play_again = "s"
    
# Definir las opciones validas
options = ["piedra", "papel", "tijera"]

while play_again.lower() == "s":
# Pedir una opcion al usuario y estandarizar a minusculas
    choice = input(f"\n{name}, introduce la opcion que deseas elegir (piedra, papel o tijera):\n")
    choice = choice.lower()

# Obtener la eleccion de la computadora aleatoriamente 
    computer = random.choice(options) 

# Si la opcion no es valida, notificar y terminar el programa.
    if choice not in options:
        print("\nOpción no valida.\n")
    
# Si la opcion es valida...
    else:
    
    # Imprimir las opciones elegidas por el usuario y la computadora
        print("\nOpciones elegidas:")
        print(f"{name}: {choice}")
        print(f"Computadora: {computer}\n")
        print("Resultado:")
    
    
    # Comparar las dos opciones
    # Si son iguales, indicar que hay un empate
        if computer == choice:
            print("¡EMPATE! :O\n")
    
    # Si el usuario elige "piedra"...
        elif choice == "piedra":
        # Usuario gana si la eleccion de la computadora es "tijera"
            if computer == "tijera":
                print(f"¡Felicidades {name}, GANASTE! :)\n")
        # Usuario pierde si la eleccion de la computadora es "papel"
            else:
                print(f"¡Lo siento {name}, PERDISTE! :(\n")
        
    # Si el usuario elige "papel"...
        elif choice == "papel":
        # Usuario gana si la eleccion de la computadora es "piedra"
            if computer == "piedra":
                print(f"¡Felicidades {name}, GANASTE! :)\n")
        # Usuario pierde si la eleccion de la computadora es "tijera"
            else:
                print(f"¡Lo siento {name}, PERDISTE! :(\n")
        
    # Si el usuario elige "tijera"...
        elif choice == "tijera":
        # Usuario gana si la eleccion de la computadora es "papel"
            if computer == "papel":
                print(f"¡Felicidades {name}, GANASTE! :)\n")
        # Usuario pierde si la eleccion de la computadora es "piedra"
            else:
                print(f"¡Lo siento {name}, PERDISTE! :(\n")
            
        
        play_again = input("¿Quieres jugar de nuevo? s/n:\n")
        