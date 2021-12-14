def pile():
    p = []
    N = int(input( "nombre d'elements de votre pile :" ))
    while N==0:
        print("Erreur, veuillez entrer un nombre supérieur à 0")
        N = int(input( "nombre d'elements de votre pile :" ))

    for i in range (N):
        p.append(int(input('ajouter un nombre :')))
        print(p)

    M = int(input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : "))
    while M!= 1 and M!=0:
        print("Erreur, veuillez entrer soit 1, soit 0")
        M = int(input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : "))
    if  M  == 1 :

        D = int(input("nombre d'elements à dépiler : "))
        while D>len(p):
            print("Erreur, veuillez entrer un nombre entre 0 et", len(p))
            D = int(input("nombre d'elements à dépiler : "))

        for i in range (D) :
            p.pop()
        print(p)

    elif M == 0 :
        print("ok :D ")
    else :
         M = int(input("voulez vous dépiler un où plusieurs elements ? 1 = oui 0 = non : "))

    if p == [] :
        print("votre fonction est vide")




pile()
