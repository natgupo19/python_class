saludo = "Buenos días"
nombre = "Andrea"
mensaje = saludo + ' ' + nombre
mensaje += '!'

print(len(mensaje)) # Funcion

print(mensaje.find('Andrea')) # Metodo

print(mensaje.find('Kevin')) # Metodo

dna = "AAGGTACGTCGCGCGTTATTAGCCTAAT"
print("El codon TAC empieza en la posición: ", dna.find('TAC'))
