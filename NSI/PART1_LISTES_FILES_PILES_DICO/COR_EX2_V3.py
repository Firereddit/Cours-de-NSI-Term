#Ex2
L1 = []
L2 = []

for i in range(4):
    L1.append(i + 1)
    L2.append(L1[i])

print("la liste L1 est:",L1)
print("La liste L2 est:",L2)