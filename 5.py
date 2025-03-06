#Crear una funció que donada una llista, retorni un diccionari que
#  tingui com a clau: els valors de la llista i com a valor el 
# seu índex dins la llista. Utilitzar enumerate.
#  Ex: (‘casa’,’cotxe’,’cadira’,’taula’) retorni {‘casa’:0, ‘cotxe’:1, ‘cadira’:2, ‘taula’:3}.
def crear_diccionari(llista):
    return {element: index for index, element in enumerate(llista)}

llista = ['casa', 'cotxe', 'cadira', 'taula']
diccionari = crear_diccionari(llista)
print(diccionari)


    