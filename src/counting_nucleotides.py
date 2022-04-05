'''
NAME
Counting DNA Nucleotides

VERSION
1.0

AUTHOR
Natalia Gutierrez Ponce

DESCRIPTION
El programa muestra cuantas A, T, C, y G se encuentran en una secuencia de DNA introducida por el usuario.

CATEGORY

USAGE

ARGUMENTS
'''

# Pedimos la secuencia de DNA al usuario
dna = input("Introduzca una secuncia de DNA: \n")

# Contamos la cantidad de nucleótidos que hay en la secuencia y lo imprimimos al usuario
print(f"La cantidad de A es: {dna.count('A')}.")
print(f"La cantidad de T es: {dna.count('T')}.")
print(f"La cantidad de C es: {dna.count('C')}.")
print(f"La cantidad de G es: {dna.count('G')}.")