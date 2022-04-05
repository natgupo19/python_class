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
DNA sequence

USAGE
El programa permite obtener la frecuencia de aparicion de cada uno de los cuatro nucleotidos
en una secuencia de DNA. Esta secuencia debe de ser introducida por el usuario.

ARGUMENTS
None

SEE ALSO
None
'''

# Pedimos la secuencia de DNA al usuario
dna = input("Introduzca una secuencia de DNA: \n")

# Contamos la cantidad de nucleótidos que hay en la secuencia y lo imprimimos al usuario
print(f"La cantidad de A es: {dna.count('A')}. \nLa cantidad de T es: {dna.count('T')}. \nLa cantidad de C es: {dna.count('C')}. \nLa cantidad de G es: {dna.count('G')}.")
