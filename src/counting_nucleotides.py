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
dna= input("Introduzca una secuencia de DNA:\n").upper()

# Realizar conteo de cada base
freq_A = dna.count('A')
freq_C = dna.count('C')
freq_G = dna.count('G')
freq_T = dna.count('T')

if (freq_A == 0 & freq_C == 0 & freq_G == 0 & freq_G == 0 or dna == ''):
    print("\nNo se introdujo una secuencia de ADN.\n")
    
else:
    # Imprimir el resultado
    print(f"""\nLa cantidad de A es: {freq_A}
La cantidad de C es: {freq_C}  
La cantidad de G es: {freq_G}  
La cantidad de T es: {freq_T}\n""")
