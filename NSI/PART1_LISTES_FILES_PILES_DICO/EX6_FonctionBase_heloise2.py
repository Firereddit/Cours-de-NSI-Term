def pile():
    p = []
    N = int(input( "nombre d'elements de votre pile :" ))
    for i in range (N):
        p.append(int(input('ajouter un nombre :')))
        print(p)

    M = int(input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : "))
    while M  != 1 and M != 0 :
        M = int(input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : "))

    print(M)

    if  M  == 1 :

        D = int(input("nombre d'elements à dépiler : "))
        while D > len(p) :
            D = int(input("nombre d'elements à dépiler : "))



        for i in range (D) :
            p.pop()
            return p

    elif M == 0 :
        print("ok :D ")
        return p

def EstVide(p):
    if len(p)==0 :
        print("est vide")
        return True
    else :
        print("n'est pas vide")
        return False




p=pile()

EstVide(p)