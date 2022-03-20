import random as rd




"""
Force brute : n = 20 objets : 2**20 combinaisons (valables ou pas)
C'est faisable... mais si n augmente, cela va se compliquer !
"""

def forceBrute(objets, w):
    """
    Résolution du problème du sac à dos par force brute
    objets est une liste d'objets du type (poids,valeur)
    w est le poids maximum entrant dans le sac
    Un nombre en binaire permet d'indiquer quels objets sont sélectionnés.
    """
    combinaison = -1
    n = len(objets)
    valeurmax = 0
    combinaisonmax = 0
    for i in range(2**n):
        poids = 0
        valeur = 0
        combinaison += 1
        combiBinaire = bin(combinaison)[2:]
        combiBinaire = (n-len(combiBinaire))*'0'+combiBinaire # avec n chiffres
        for j in range(n):
            if combiBinaire[j] == '1':
                poids += objets[j][1]
                if poids > w:
                    break
                valeur += objets[j][0]
        else:
            if valeur > valeurmax:
                valeurmax = valeur
                combinaisonmax = combiBinaire
    contenuSac = []
    for j in range(n):
        if combinaisonmax[j] == '1':
            contenuSac.append(objets[j])
    return valeurmax, contenuSac
        



"""
Programmation dynamique
"""
def tableau_kp_dynamique(objets,w):
    """
    Résolution du problème du sac à dos par programmation dynamique
    >>> tableau_kp_dynamique([(3, 2), (8, 10), (2, 2), (8, 1), (4, 6), (6, 6)], 10)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 8]
    [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 8]
    [0, 8, 8, 11, 11, 13, 13, 13, 13, 13, 13]
    [0, 8, 8, 11, 11, 13, 13, 13, 13, 15, 15]
    [0, 8, 8, 11, 11, 13, 13, 14, 14, 17, 17]
    """
    n= len(objets)
    tab= [[0]*(w+1) for i in range(n+1)]
    for i in range(n):
        for e in range(w+1):
            x, y= objets[i]
            if e>= y:
                tab[i+1][e]= (max(tab[i][e],tab[i][e-y]+x))
            else:
                tab[i+1][e]= (tab[i][e])
    return tab

def kp_dynamique(objets, w):
    """
    Renvoie la valeur maximale et une liste d'objets réalisant cette valeur
    en utilisant le tableau renvoyé par la fonction tableau_kp_dynamique
    """
    tab = tableau_kp_dynamique(objets, w)
    contenu=[]
    y=int(len(tab[0]) - 1)
    e=int(len(tab) - 1)
    valeur=tab[e][y]
    
    while e > 0:
        if tab[e - 1][y] == tab[e][y]:
            pass
        
        else:
            v, p = objets[e]
            contenu.append((v, p))
            y=y-p
            
        e-=1
    return valeur, contenu

def test_dynamique(ntest=10, n=15, w=20, vmax=15, pmax=8):
    """
    Teste la fonction kp_dynamique
    """
    for i in range(ntest):
        objets = [(rd.randrange(vmax)+1, rd.randrange(pmax)+1) for i in range(n)]
        fb = forceBrute(objets, w)  
        dyn = kp_dynamique(objets, w)
        if fb[0] != dyn[0] or sum(ob[1] for ob in dyn[1]) > w or sum(ob[0] for ob in dyn[1]) != dyn[0]:
            print('Test failed with', objets, 'and', w)
            return
    print('Test OK')
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


