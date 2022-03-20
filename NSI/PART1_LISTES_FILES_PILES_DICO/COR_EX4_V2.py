#Ex4

print("-------Ex4-------")

F1 = ["A", "B", "C", "D", "E"]

print("Si on défile F1, on obtient", (F1.pop(0)))

F1 = ["A", "B", "C", "D", "E"]

F1.reverse()
P1 = []
P2 = []

#Défilage de F1
for i in range(len(F1)):
    P1.append(F1.pop(0))
    print(P1)

#Dépilage de P1
for i in range(len(P1)):
    P2.append(P1.pop())
    print(P2.pop()) #Dépilage de P2