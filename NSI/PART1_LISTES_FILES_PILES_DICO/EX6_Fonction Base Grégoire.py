##PILES##

def CREER_PILE():
    """Fonction qui crée une pile nommée "pile", et la renvoie."""
    pile = []
    return pile

def EMPILER(pile, n):
    """Fonction qui ajoute un élément à la fin de la pile et qui la renvoie après l'avoir empilé."""
    pile.append(n)
    return pile

def DEPILER(pile):
    """Fonction qui enlève le premier élément de la pile et qui la renvoie après l'avoir dépilé."""
    pile.pop()
    return pile

##FILES##

def CREER_FILE():
    """Fonction qui crée une file nommée "file", et la renvoie."""
    file = []
    return file

def ENFILER(file, n):
    """Fonction qui ajoute un élément au début de la file et qui la renvoie après l'avoir enfilé."""
    file.append(n)
    return file

def DEFILER(file):
    """Fonction qui enlève le premier élément de la pile et qui la renvoie après l'avoir dépilé."""
    file.pop(0)
    return file

##LISTE##

def EST_VIDE(pile):
    """Fonction qui vérifie si une liste (file ou pile) est vide. Elle revoie le booléen "True si c'est le cas, "False" si ça ne l'est pas."""
    if len(pile) == 0:
        return True
    else:
        return False