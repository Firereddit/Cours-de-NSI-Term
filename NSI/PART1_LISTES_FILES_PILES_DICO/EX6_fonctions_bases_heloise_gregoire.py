def P_EDITOR():
    print("---Éditeur de pile---")
    creation_pile()
    depilage()

def creation_pile():
    global pile
    pile = []

    L = int(input("Entrez la longueur de la pile que vous voulez créer: \n"))
    for i in range(L):
        V = int(input(f"Entrez la valeur à l'index {i+1}: "))
        pile.append(V)
        print(pile)

def depilage():
    R = input("Voulez-vous dépiler un ou plusieurs éléments? oui/non \n")
    if R == "oui":
        depilageq()
    elif R == "non":
        print("Ok! Pile créée avec succès.")
    else:
        print("Réponse invalide! Veuillez utiliser oui ou non.")
        depilage()  

def depilageq():
    R1 = int(input("Combien d'éléments voulez-vous dépiler? \n"))
    if R1 >= 1 and R1 <= len(pile):
        for i in range(R1):
            pile.pop()
        print(pile)
        findepilage()
    elif R1 > len(pile):
        print("Vous ne pouvez pas dépiler plus d'éléments que la longueur de la pile!")
        depilageq()
    else:
        print("Ce n'est pas un chiffre valide!")
        depilageq()
    
def findepilage():
    if pile == []:
        print("Pile vide!")
    else:
        print("Terminé")

P_EDITOR()