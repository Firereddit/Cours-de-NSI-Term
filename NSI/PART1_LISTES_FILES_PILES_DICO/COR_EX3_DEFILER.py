#Défiler un file => FIFO
def ex3():
    F = []
    F.append(4)
    F.append(1)
    F.append(3)

    N = F.pop(0)

    F.append(8)

    N = F.pop(0)

    print ("la file est:",F,"l'élément sorti de la file est:", N)


print ("Exercice3:-----------------")
ex3()