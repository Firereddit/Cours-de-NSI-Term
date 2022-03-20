
def CreerPile():
    """Cette fonction va créer une pile, P puis la renvoyer"""
    P = []
    return P

def Empiler(Pile, x):
    """cette fonction permet d'empiler les valeurs de la file/pile/liste dans une pile
    elle retournera une pile du nom de PEmpilee"""
    Pile.append(x)
    return Pile

def Depiler(Pile, n):
    """cette fonction permet de dépiler une liste et va renvoyer le premier élément dépilé
    Pour dépiler une liste entière, il faut metter cette fonction dans une boucle, le cas échéant, elle ne renverra que la première valeur de la pile sous le nom de 'varDepilee'"""
    varDepilee = Pile.pop(n)
    return varDepilee

def PEstVide(Pile):
    """Cette fonction renverra True si la pile est vide et False si elle ne l'est pas"""
    if len(Pile) == 0:
        return True
    else:
        return False



def CreerFile():
    """Cette fonction va créer une file, F puis la renvoyer"""
    F = []
    return F

def Enfiler(File, x):
    """cette fonction permet d'enfiler la valeur de x dans la file"""
    File.reverse()
    File.append(x)
    File.reverse()
    return File

def Defiler(File, x):
    """cette fonction permet de défiler une liste et va renvoyer le premier élément dépilé
    Pour défiler une liste entière, il faut metter cette fonction dans une boucle, le cas échéant, elle ne renverra que la première valeur de la file sous le nom de 'varDefilee'"""
    varDefilee = File.pop(x)
    return varDefilee

def FEstVide(File):
    """Cette fonction renverra True si la file est vide et False si elle ne l'est pas"""
    if len(File) == 0:
        return True
    else:
        return False