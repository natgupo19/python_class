'''
NAME
Sequences to fasta

VERSION
1.0

AUTHOR
Natalia Gutierrez Ponce

GITHUB
https://github.com/natgupo19/python_class

DESCRIPTION
El programa toma un archivo de secuencias de DNA y crea un archivo en formato FASTA con el mismo contenido.

CATEGORY
FASTA format

USAGE
py .\src\sequences_to_fasta.py

ARGUMENTS
None

INPUT
Archivo: data/dna_sequences.txt

OUTPUT
Archivo: data/dna_sequences.fasta

SEE ALSO
None
'''
#Agregamos la estructura try-except para notificar al usuario si es que el archivo no se encuentra en la ruta marcada.
try:
    # Abrimos el archivo
    my_file = open('./data/dna_sequences.txt')

    # Leemos todas las lineas y las guardamos en una lista
    all_lines = my_file.readlines()
    
    # Cerramos el archivo
    my_file.close()

except IOError as Io_Error:
    print(f"\nLa ruta {Io_Error.filename} no es valida, el archivo que desea leer no fue encontrado.\n")

else:
    # Creamos el archivo fasta
    my_file2 = open('./results/dna_sequences.fasta', 'w')

    # Recorremos la lista con un loop
    # Separamos los IDs de las secuencias con un split
    # Convertimos todos los caracteres de las secuencias a mayusculas y eliminamos los guiones '-', si es que existen
    # Escribimos en el archivo creado con el formato requerido para crear el fasta
    for line in all_lines:
        elements = line.split(' ')
        id = elements[0]
        seq = elements[-1].upper().replace('-', '')
        my_file2.write(f"> {id}\n{seq}")
    
    # Cerramos el archivo creado
    my_file2.close()

    # Indicamos al usuario la ruta en donde se guardo el archivo creado
    print("\nLa ruta en la que se encuentra el archivo creado es: ./results/dna_sequences.fasta\n")