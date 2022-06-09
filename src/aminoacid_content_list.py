'''
NAME
    aminoacid_content

VERSION
    1.0

AUTHOR
    Natalia Gutierrez Ponce

GITHUB
    https://github.com/natgupo19/python_class

DESCRIPTION
    Calcula el porcentaje de cada elemento de una lista de aminoacidos en una secuencia proteica 

CATEGORY
    Protein sequence

USAGE
    py .\src\aminoacid_content.py [-h] -s SEQUENCE [-a AMINOACIDS]
    [-o path/to/output/file] [-r ROUND]

ARGUMENTS
    -h, --help          Show this help message and exit
    -s SEQUENCE, --sequence SEQUENCE
                        Protein sequence to analyze
    -a AMINOACIDS, --aminoacids AMINOACIDS
                        Amino acids to search (single-letter code)
    -o path/to/output/file, --output path/to/output/file
                        Path for the output file
    -r ROUND, --round ROUND
                        Number of digits to round

INPUT
    Secuencia de aminoacidos a analizar

SEE ALSO
    aminoacid_content.py
'''

import argparse
from itertools import count

# Crear el parser
parser = argparse.ArgumentParser(description = "Script que calcula el contenido de un\
                                aminoacido en particular patir de una secuencia proteica.")

# Agregar y almacenar los argumentos
parser.add_argument("-s", "--sequence",
                    help="Protein sequence to analyze",
                    type=str,
                    required=True)
                    
parser.add_argument("-a", "--aminoacids",
                    help="Amino acids to search",
                    type=list,
                    required=False)

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    required=False)
                    
parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)
  
args = parser.parse_args()

# Declaramos la funcion
# Estandarizamos a mayusculas
def aminoacid_percentage(protein_sequence, aminoacid_list = ['A','I','L','M','F','W','Y','V']):
    '''
    Devuelve el porcentage de una lista de aminoacidos en una secuencia proteica
    
        Parametros:
                    protein_sequence (str): secuencia proteica 
                    aminoacid_list (list): lista de aminoacidos
        Devuelve:
                    acumulated_percentage (int): porcentaje de aminoacidos de la lista en la secuencia proteica
    '''
    protein_sequence = protein_sequence.upper() 
    
    # Inicializamos el contador a cero
    acumulated_percentage = 0

    # Calculamos el porcentaje de cada aminoacido de la lista en la secuencia
    # Regresamos el porcentaje acumulado
    for aminoacid in aminoacid_list:
        aminoacid = aminoacid.upper()
        aminoacid_count = protein_sequence.count(aminoacid)
        sequence_length = len(protein_sequence)
        percentage = (aminoacid_count * 100) / sequence_length
        acumulated_percentage += percentage
    return acumulated_percentage
 
# Comprobar que la funcion funcione correctamente con el assert   
try: 
    assert aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP") == 65

except AssertionError as AssertionError:
    print("Algo salio mal\n")

# Estandarizamos a mayusculas
sequence = args.sequence.upper()

# Si el usuario da la lista de aminoacidos 
if args.aminoacids:  
    aminoacid_list = args.aminoacids
    percentage = aminoacid_percentage(sequence, aminoacid_list)
    
    # Redondear el porcentaje si fue solicitado por el usuario
    if args.round:
        percentage = round(percentage, args.round)
    
    # Imprimir el porcentaje en el archivo indicado por el usuario si asi lo requiere
    if args.output:
        with open(args.output, 'w') as output_file:
            print(f"\nSecuencia proteica: {sequence} \
                    \nAminoacidos: {aminoacid_list} \
                    \nContenido de {aminoacid_list} en la secuencia: {percentage} %",
                    file=output_file)
                  
        print(f"\nSe ha generado el archivo {args.output} con el contenido de {aminoacid_list}.\n")
        
    # Se imprime el contenido de aminoacidos hidrofilicos en la secuencia dada  
    else:
        print(f"\nSecuencia proteica: {sequence} \
                \nAminoacidos: {aminoacid_list} \
                \nContenido de {aminoacid_list} en la secuencia: {percentage} %\n")
            
# Si el usuario no da la lista de aminoacidos... 
else:
    percentage = aminoacid_percentage(sequence)
    
    # Redondear el porcentaje si fue solicitado por el usuario
    if args.round:
        percentage = round(percentage, args.round)
        
    # Imprimir el porcentaje en el archivo indicado por el usuario si asi lo requiere
    if args.output:
        with open(args.output, 'w') as output_file:
            print(f"\nSecuencia proteica: {sequence} \
                    \nAminoacidos hidrofilicos: A, I, L, M, F, W, Y, V \
                    \nContenido de aminoacidos en la secuencia: {percentage} %\n",
                    file=output_file)
                    
        print(f"\nSe ha generado el archivo {args.output} con el contenido de: A, I, L, M, F, W, Y, V.\n")
        
    # Se imprime el contenido de aminoacidos hidrofilicos en la secuencia dada
    else:
        print(f"\nSecuencia proteica: {sequence} \
                \nAminoacidos hidrofilicos: A, I, L, M, F, W, Y, V \
                \nContenido de aminoacidos en la secuencia: {percentage} %\n")
    




