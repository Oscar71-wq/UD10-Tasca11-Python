#Crear una funció que donada una llista de paraules i una lletra, retorni una llista amb les paraules que comencen per la lletra donada. 
#Utilitzar filter. Ex: [“maria”, “manta”, “peu”, “mà”] i li deim que ens retorni totes les que comencen per ‘p’, en retorni [‘peu’].


def paraules_comencen_lletra(paraules, lletra):
    return list(filter(lambda paraula: paraula.startswith(lletra), paraules))

def llista():
    entrada_paraules = input("Introdueix una llista de paraules separades per espais: ")
    
    paraules = entrada_paraules.split()
    
    lletra = input("Introdueix una lletra: ")
    
    resultat = paraules_comencen_lletra(paraules, lletra)
    
    print(f"Les paraules que comencen amb '{lletra}' són: {resultat}")

llista()