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
python count_nucleotides.py

ARGUMENTS
None

SEE ALSO
None
'''

# Obtener la secuencia de ADN del usuario
dna= input("Introduzca una secuencia de DNA:\n")

# Realizar conteo de cada base
freq_A = dna.count('A')
freq_C = dna.count('C')
freq_G = dna.count('G')
freq_T = dna.count('T')

# Imprimir el resultado
print(f"""La cantidad de A es: {freq_A}
La cantidad de C es: {freq_C}  
La cantidad de G es: {freq_G}  
La cantidad de T es: {freq_T}""")
