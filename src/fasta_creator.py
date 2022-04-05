'''
NAME
Fasta creator

VERSION
1.0

AUTHOR
Natalia Gutierrez Ponce

DESCRIPTION
El programa crea un archivo fasta que contenga una secuencia de DNA que se encuentra en un archivo txt

CATEGORY

USAGE

ARGUMENTS
'''

# Accedemos a la secuencia del archivo solicitado
seq = open("data/dna.txt")

# Leemos el contenido del archivo
seq_contents = seq.read()

# Cerramos el open
seq.close()

# Abrimos y creamos el archivo fasta
my_file = open("data/dna.fasta", "w")

# Escribimos lo que irá dentro del archivo
my_file.write(">sequence_name \n")
my_file.write(seq_contents)