def demande():
    global M
    M = input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : ")
    if not M:
        print (f'veuillez entrer un nombre')
        demande()
    else:
        M = int(M)
    if M != 1 and M != 0:
        print (f"Caractère invalide, veuillez entrer 1 ou 0")
        demande()
    return M



def eltADepiler():
    global D
    D = int(input("nombre d'elements à dépiler : "))

    if D <= len(p):
        for i in range (D) :
            p.pop()
            print(p)
    else:
        print (f"Nombre trop grand, le nombre maximale que vous pouvez dépiler est {N}")
        eltADepiler()
    return D



def pile():
    global p, N
    p = []
    N = input( "nombre d'elements de votre pile :" )
    if not N:
        print (f'veuillez entrer un nombre')
        pile()
    for i in range (N):
        p.append(int(input('ajouter un nombre :')))
        print(p)

    demande()
    
    if  M  == 1 :
        eltADepiler()

    elif M == 0 :
        print("ok :D ")

    if len(p) == 0:
        return True
    else :
        return False

pile()