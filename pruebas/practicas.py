import sys
#version de py
"""
print (sys.version)

print(sys.version_info)
"""
#saltos de linea 
print("ejemplo", end="")
print("ejemplo") # el end hizo que se concatenaran las lineas, no salto de linea  
print("ejemplo", "de" ,"separeitor(sep)", sep="*") #hace que en el espacio de lineas introdusca el caracquer que le indiques
#place holder
print("{} ejemplo {}".format("arroz","potro"))
#arreglo
print()
numeros=[1,2,4,5,9]
print(numeros)

#cadena de caracteres al reves 
print()
cadena = "lola"
for i in range(len(cadena)-1 , -1 , -1):
    print(cadena[i], end="") 

print ()
#otro metodo mas facil sin ciclo for
print(cadena[::-1])


#OBTENER LISTA DE NUMEROS SEPARADOS POR COMA Y CREAR LISTA
#

numeros = input("Dame una lista de numeros separados por coma: ")

print(numeros)

lista=numeros.split(",")
print(lista)
print(type(lista))

#OBTENER LA EXTENSION DE UN ARCHIVO ESPECIFICADO POR USUARIO
#

name_file=input("Ingrese el nombre del archivo: ")

partes_name_file =name_file.split(".")
print(partes_name_file)