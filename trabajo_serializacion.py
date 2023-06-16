import pickle
# con este codigo creamos el archivo lista_nombres y cargamos los nombres del archivo fichero_binario
"""lista_nombres=["Pedro","Ana","Maria","Isabel"]
fichero_binario=open("lista_nombres","wb")
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()
del (fichero_binario)"""

# con este codigo recuperamos los nombres de la lista_nombres a la variable lista
"""fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)"""