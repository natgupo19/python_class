'''
NAME
AT and GC percentage

VERSION
1.0

AUTHOR
Natalia Gutierrez Ponce

DESCRIPTION
El programa calcula el porcentaje de GC y AT en una secuencia de DNA.

CATEGORY

USAGE

ARGUMENTS
'''

# Solicitamos la ruta donde se encuentra el archivo con la secuencia de DNA
ruta = input("Introduzca la ruta del archivo en donde se encuentra la secuencia de DNA: \n")

# Accedemos a la secuencia del archivo solicitado
my_file = open(ruta)

# Leemos el contenido del archivo
my_file_contents = my_file.read()

# Quitamos el caracter de salto de linea \n
my_dna = my_file_contents.rstrip("\n")

# Contamos la cantidad de nucleotidos en la secuencia
nucleotidos = len(my_dna)

# Calculamos el porcentaje de AT y GC en la secuencia con una regla de 3
AT = ((my_dna.count('A') + my_dna.count('T')) * 100) / (nucleotidos)
GC = ((my_dna.count('A') + my_dna.count('T')) * 100) / (nucleotidos)

# Imprimimos el porcentaje de AT y GC al usuario
print(f"El porcentaje de AT en la secuencia es: %{AT}")
print(f"El porcentaje de GC en la secuencia es: %{GC}")

# Cerramos el open
my_file.close()