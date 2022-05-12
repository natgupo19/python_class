'''
NAME
    AT and GC percentage

VERSION
    4.0

AUTHOR
    Natalia Gutierrez Ponce

GITHUB
    https://github.com/natgupo19/python_class

DESCRIPTION
    El programa calcula el porcentaje de GC y AT en una secuencia de DNA.

CATEGORY
    DNA sequence

USAGE
    py .\src\AT_GC_percentage.py
    
ARGUMENTS
    None

INPUT
    Ruta y nombre de un archivo que contiene una secuencia de DNA
    Nota: Los archivos con datos para programas se hallan en data/

OUTPUT
    Porcentaje de AT y GC en la secuencia de DNA

SEE ALSO
    None
'''

# Importamos la biblioteca
import argparse

# Creamos el parser
parser = argparse.ArgumentParser(description = "Script que calcula el porcentaje de AT y GC a partir de \
                                                la ruta de un archivo que contiene una secuencia de DNA.")
                                           
# Agregamos y almacenamos los argumentos
parser.add_argument("-i", "--input",
                    metavar="path/to/input/file",
                    help="File with gene sequences",
                    required=True)

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    required=False)
                    
parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)
  
args = parser.parse_args()

# Leemos la ruta en la que se encuentra el archivo con la secuencia
ruta = args.input

# Agregamos la estructura try-except para infromar al usuario si la ruta en la que se encuentra el archivo no es valida
try: 
    # Accedemos a la secuencia del archivo solicitado
    my_file = open(ruta)

    # Leemos el contenido del archivo
    my_file_contents = my_file.read()

    # Quitamos el caracter de salto de linea \n
    my_dna = my_file_contents.rstrip("\n")

    # Contamos la cantidad de nucleotidos en la secuencia
    nucleotidos = len(my_dna)
    
    # Cerramos el open
    my_file.close()
    
except IOError as Io_Error:
    print(f"\nLa ruta {Io_Error.filename} no es valida, el archivo que desea leer no fue encontrado.\n")

else:
    # Calculamos el porcentaje de AT y GC en la secuencia con una regla de 3
    at_percentage = ((my_dna.count('A') + my_dna.count('T')) * 100) / nucleotidos
    gc_percentage = ((my_dna.count('G') + my_dna.count('C')) * 100) / nucleotidos

    # Redondeamos el resultado si es que asi se especifica
    if args.round: 
        at_percentage = round(at_percentage, args.round)
        gc_percentage = round(gc_percentage, args.round)
    
    # Generamos un archivo con los resultados si asi se desea
    if args.output:
        with open(args.output, 'w') as output_file:
            print(f"La secuencia de DNA es: {my_dna} \
                    \nEL porcentaje de AT en la secuencia es: {at_percentage} % \
                    \nEl porcentaje de GC en la secuencia es: {gc_percentage} %", 
                    file = output_file)
        print(f"\nSe genero el archivo {args.output} con los resultados obtenidos.\n")    
    
    # Imprimimos el porcentaje de AT y GC al usuario
    else:
        print(f"\nLa secuencia de DNA es: {my_dna} \
                \nEl porcentaje de AT en la secuencia es: {at_percentage} % \
                \nEl porcentaje de GC en la secuencia es: {gc_percentage} %\n")

    
