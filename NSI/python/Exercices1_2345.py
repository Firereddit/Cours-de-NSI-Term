def ex2():
    l1 = []
    l2 = []

    for i in range (4):
        l1.append(i+1)

    for i in range (4):
        l2.append(l1[i])

    print(l1, l2)

def ex3():
    F = []
    F.append(4)
    F.append(1)
    F.append(3)

    N = F.pop(0)

    F.append(8)

    N = F.pop(0)

    print (F, N)

def ex4_1():
    F1 = ['A', 'B', 'C', 'D', 'E']
    print(f"un défilage de F1 est donc: {F1.pop(0)}")
def ex4_2():
    F1 = ['A', 'B', 'C', 'D', 'E']
    P1 = []
    P2 = []

    for i in range (len(F1)):
#         En utilisant la fonction pop() pour la liste F1, on admet que F1 est une Pile et non une file comme demandé dans l'exercice
        P1.append(F1.pop())
        print(P1)
    for i in range (len(P1)):
        P2.append(P1.pop())
        print(P1, P2)

def ex4_Non_Pile():
    F1 = ['A', 'B', 'C', 'D', 'E']
    P1 = []
    P2 = []

    for i in range (len(F1)):
        P1.append(F1[len(F1)-len(F1)-i-1])
        print(P1)
    print("""            |
            |
            |
            |
 ____________
 |
 V""")
    for i in range (len(P1)):
        P2.append(P1.pop())
        print(P2.pop())



def ex5():
    # operande1 = 0
    # operande2 = 0
    # operateur = ''
    # LNPI = ['3','2','+','13','*']
    # LNPIFinal = []
    #
    # for i in range(len(LNPI)):
    #     operande1 = LNPI.pop(0)
    #     operande2 = LNPI.pop(0)
    #     print(operande1, operande2)
    #
    #     if '+' in LNPI:
    #         operateur = LNPI.pop(0)
    #         resultat = (int(operande1) + int(operande2))
    #         print(resultat)
    #     elif '+' in LNPI:
    #         operateur = LNPI.pop(0)
    #         resultat = (int(operande1) - int(operande2))
    #         print(resultat)
    #     elif '+' in LNPI:
    #         operateur = LNPI.pop(0)
    #         resultat = (int(operande1) * int(operande2))
    #         print(resultat)
    #     elif '+' in LNPI:
    #         operateur = LNPI.pop(0)
    #         resultat = (int(operande1) / int(operande2))
    #         print(resultat)
    #
    #     int(resultat)
    #     LNPI.reverse()
    #     LNPI.append(resultat)
    #     LNPI.reverse()
    #     print
    #
    #
    #     print(LNPI, LNPIFinal)
    #
    #
    # print(resultat)

    print(f"Correction sur Teams")




print ("Exercice2:-----------------")
ex2()
print ("Exercice3:-----------------")
ex3()
print ("Exercice4:-----------------")
ex4_1()
ex4_2()
ex4_Non_Pile()
print ("Exercice5:-----------------")
ex5()