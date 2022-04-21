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

# Declarar el random
import random

# Bienevneida y peticion de nombre
print("\n¡Bienvenidx al juego de piedra, papel o tijera!\n")
name = input("Introduce tu nombre:\n")

# Lista con opciones posibles
options = ["piedra", "papel", "tijera"]

# Pedimo la opcion al usuario
choice = input(f"\n{name}, introduce la opcion que deseas elegir (piedra, papel o tijera):\n")
choice = choice.lower()

# Opcion computadora
computer = random.choice(options) 

# Si la opcion no es valida, notificar.
if choice not in options:
    print("\nOpción no valida.\n")
    
# S i la opcion es valida...
else:
    
    # Imprimir las opciones elegidas por cada quien
    print("\nOpciones elegidas:")
    print(f"{name}: {choice}")
    print(f"Computadora: {computer}\n")
    print("Resultado:")
    
    # Si es la misma opcion notificar empate
    if computer == choice:
        print("¡EMPATE! :O\n")
    
    # S i elige piedra
    elif choice == "piedra":
        if computer == "tijera":
            print(f"¡Felicidades {name}, GANASTE! :)\n")
        else:
            print(f"¡Lo siento {name}, PERDISTE! :(\n")
        
    # Si elige papel
    elif choice == "papel":
        if computer == "piedra":
            print(f"¡Felicidades {name}, GANASTE! :)\n")
        else:
            print(f"¡Lo siento {name}, PERDISTE! :(\n")
        
    # Si elige tijera
    elif choice == "tijera":
        if computer == "papel":
            print(f"¡Felicidades {name}, GANASTE! :)\n")
        else:
            print(f"¡Lo siento {name}, PERDISTE! :(\n")
            