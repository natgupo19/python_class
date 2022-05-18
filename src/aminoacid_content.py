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
    None
'''

import argparse

# Crear el parser
parser = argparse.ArgumentParser(description = "Script que calcula el \
           contenido de una lista de aminoacidos a patir de una secuencia proteica.")

# Agregar y almacenar los argumentos
parser.add_argument("-s", "--sequence",
                    help="Protein sequence to analyze",
                    type=str,
                    required=True)
                    
parser.add_argument("-a", "--aminoacid",
                    help="Amino acid to search",
                    type=str,
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

def aminoacid_content(protein_sequence, aminoacid):
    protein_length = len(protein_sequence)
    content = (protein_sequence.upper().count(aminoacid.upper()) *100) / protein_length
    return(content)

assert aminoacid_content("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert aminoacid_content("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert aminoacid_content("msrslllrfllfllllpplp", "L") == 50
assert aminoacid_content("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

amino = args.aminoacid
sequence = args.sequence

percentage = aminoacid_content(sequence, amino)

# Redondear el porcentaje si fue solicitado por el usuario
if args.round:
    percentage = round(percentage, args.round)

# Imprimir el porcentaje en el archivo indicado por el usuario
if args.output:
    with open(args.output, 'w') as output_file:
        print(f"Secuencia proteica: {sequence} \
                \nAminoacido: {amino} \
                \nContenido de {amino} en la secuencia: {percentage} %",
                file=output_file)
                  
    print(f"\nSe ha generado el archivo {args.output} con \
            el contenido de {amino}.\n")

# Imprimir resultado a pantalla si no fue solicitado un archivo output
else:
    print(f"\nSecuencia proteica: {sequence} \
            \nAminoacido: {amino} \
            \nContenido de {amino} en la secuencia: {percentage} %\n")
        