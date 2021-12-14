"""
Exercice bilan 1.1
"""
# On définit la fonction "verifier" qui prend en paramètres une chaîne de caractères contenant uniquement des parenthèses ouvrantes et fermantes et qui retourne Vrai si le nombre de parenthèses ouvrantes est égal au nombre de parenthèses fermantes sinon Faux si c'est le cas contraire. La fonction renvoie également la position de ces caractères.
# Il faut parcourir la chaîne de gauche à droite. On empile chaque parenthèse ouvrante et on dépile chaque parenthèse fermante.

def verifier(chaine):
    position = 0 # On définit la position du premier caractère à 0
    pile = [] # On initialise une pile vide
    erreur = False # La fonction renvoie False de base, tant que toute la liste n'a pas été entièrement parcourue
    for parenthese in chaine : # Pour chaque caractère de la chaîne :
        if (parenthese == "("): # Si il s'agit d'une parenthèse ouvrante,
            pile.append(position) # On l'empile
        elif (parenthese == ")"): # Sinon, si il s'agit d'une parenthèse fermante,
            if (len(pile) > 0): # Et que tant que la longueur de la pile est supérieure à 0
                positionOuvre = pile.pop() # On dépile et on attribue sa position
                print ("(",positionOuvre,",",position,")") # On affiche la position de chaque couple de parenthèses (ouvrantes et fermantes)
            else : # sinon,
                erreur = True # La fonction renvoie True
        position = position + 1 # On parcourt la suite de la liste
    if (len(pile) != 0): # Si la longueur de la pile est différente de 0,
        erreur = True # On renvoie True,
    return not erreur # Et on ne retourne pas False

print (verifier("(())())")) # On met en application cette fonction avec cette suite de parenthèses. La fonction renvoie False, car les parenthèses sont mal positionnées
print (verifier("()()()((())())")) # Idem. La fonction renvoie ici True, donc les parenthèses sont bien positionnées.

print (verifier(input("Entrer une série de parenthèses"))) # Ici, l'utilisateur peut entrer lui-même sa série de parenthèses.