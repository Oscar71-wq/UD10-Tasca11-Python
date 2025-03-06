#Crear una funció que donada una llista de valors numèrics,
#retorni el número d’elements on coincideix el valor i l’índex
#on és. Utilitzar enumerate. Ex: [0, 2, 3, 3, 4], retorni 3.
def comptar_coincidencies(llista):
    return sum(1 for index, value in enumerate(llista) if index == value)

llista = [0, 2, 3, 3, 4]
resultat = comptar_coincidencies(llista)
print(resultat)
