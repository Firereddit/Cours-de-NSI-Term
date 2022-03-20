#exercice 4 utilisation des files et piles en même temps
def ex4_1():
    F1 = ['A', 'B', 'C', 'D', 'E']
    print(f"un défilage de F1 est donc: {F1.pop(0)}")
def ex4_2():
    F1 = ['A', 'B', 'C', 'D', 'E']
    P1 = []
    P2 = []

    for i in range (len(F1)):
#         En utilisant la fonction pop() pour la file F1, on admet que F1 est une Pile et non une file comme demandé dans l'exercice
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

    for i in range (len(P1)):
        P2.append(P1.pop())
        print(P2.pop())



print ("Exercice4_1:-----------------")
ex4_1()
print ("Exercice4_2:-----------------")
ex4_2()
print ("Exercice4_Non_Pile:-----------------")
ex4_Non_Pile()

