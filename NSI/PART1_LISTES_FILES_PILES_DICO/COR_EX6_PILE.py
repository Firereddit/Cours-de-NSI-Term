#fonctions de base pour une pile
def creer_pile():
    pile=[]
    return pile

def empiler(p, x):
    p.append(x)


def depiler(p):
    return p.pop()


def est_vide(p):
    if len(p) != 0:
        return False
    else:
        return True

pile_test=creer_pile()
empiler(pile_test, 'C')
empiler(pile_test, 'B')
empiler(pile_test, 'A')
print(depiler(pile_test))




