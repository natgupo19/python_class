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
DNA Sequence

USAGE
El programa permite generar un archivo en formato fasta a partir de un archivo de texto plano que contenga una
secuencia de DNA. El archivo fasta se guaradara en una carpeta llamada data.

ARGUMENTS
None

SEE ALSO
None
'''

# Agregamos la estructura try-except para notificar al usuario si es que el archivo no se encuentra en la ruta marcada
try:
    # Accedemos a la secuencia del archivo solicitado
    seq = open("./data/dna.txt")

    # Leemos el contenido del archivo
    seq_contents = seq.read()

    # Cerramos el open
    seq.close()

except IOError as Io_Error:
    print(f"\nLa ruta {Io_Error.filename} no es valida, el archivo que desea leer no fue encontrado.\n")
    
else:
    # Abrimos y creamos el archivo fasta
    my_file = open("./results/dna.fasta", "w")

    # Escribimos lo que ira dentro del archivo
    my_file.write(">sequence_name \n")
    my_file.write(seq_contents)

    # Cerramos el open
    my_file.close()

    # Imprimimos la ruta en donde se encuentra el archivo al usuario
    print("\nLa ruta en la que se encuentra el archivo creado es: ./results/dna.fasta\n")
