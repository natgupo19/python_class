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
El programa toma un archivo con secuencias de DNA y genera otro archivo con las mismas secuencias pero sin adaptadores. Nota: se sabe que los adaptadores se encuentran en las primeras 14 posiciones.

CATEGORY
DNA sequence

USAGE
py .\src\adapter_remover.py

ARGUMENTS
None

INPUT
Archivo: data/4_input_adapters.txt

OUTPUT
Archivo: data/seq_wo_adapters.txt

SEE ALSO
None
'''

# Abrimos el archivo
my_file = open('../data/4_input_adapters.txt')

# Leemos todas las lineas y las guardamos en una lista
all_lines = my_file.readlines()

# Cerramos el archivo
my_file.close()

# Creamos un nuevo archivo que almacene las secuencias sin adaptadores
my_file2 = open('../results/seq_wo_adapters.txt', 'w')

# Recorremos la lista con un loop
# Eliminar los primeros 14 elementos de cada string de la lista
# Escribir las secuencias sin adaptadores en el nuevo archivo
for line in all_lines:
  seq = line[14:]
  my_file2.write(seq)

# Cerramos el archivo creado
my_file2.close()

# Indicamos al usuario la ruta en donde se guardo el archivo creado
print("La ruta en la que se encuentra el archivo creado es: ../results/seq_wo_adapters.txt")
