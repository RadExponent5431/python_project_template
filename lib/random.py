# Own Code or librarys can be placed here


# Here replacing big parts of the random library, with simple code

from time import time

def randint(a: int, b: int):
    # Verwende die aktuelle Zeit als Seed
    seed = int((time() * 1000) % 1000)
    
    # Berechne eine pseudozufällige Zahl zwischen a und b
    pseudo_zufall = ((seed * 1103515245) + 12345) % 32768
    
    # Skaliere die pseudozufällige Zahl auf den Bereich zwischen a und b
    zufall_zahl = a + (pseudo_zufall % (b - a + 1))
    
    return zufall_zahl

def choice(liste: dict):
    if not liste:
        return None
    index = randint(0, len(liste) - 1)
    return liste[index]