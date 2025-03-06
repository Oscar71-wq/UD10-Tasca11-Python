def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as fitxer:
            contingut = fitxer.read()
        return contingut
    except FileNotFoundError:
        return f"Error: el fitxer '{nom_fitxer}' no existeix."
    except IOError:
        return "Error: hi ha hagut un problema en obrir el fitxer."
