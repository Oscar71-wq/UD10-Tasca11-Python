#Crear una funció que donades dues llistes, les concateni amb un connector. 
# Utilitzar zip. Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’].
def llista():
    l = ["agarre", "tomate"]
    a = ["melpino", "esta"]

    for e, j in zip(a,l):
        print("resultat {}-{}".format(j,e))

llista()

#el zip lee las listas a la vez 