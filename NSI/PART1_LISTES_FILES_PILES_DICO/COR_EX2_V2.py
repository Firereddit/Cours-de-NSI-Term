def ex2():
    l1 = []
    l2 = []

    for i in range (4):
        l1.append(i+1)

    for i in range (4):
        l2.append(l1[i])

    print("La liste L1 est:",l1,"la liste L2 est:", l2)


print ("Exercice2:-----------------")
ex2()