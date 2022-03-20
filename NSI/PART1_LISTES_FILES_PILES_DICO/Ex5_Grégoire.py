#Ex5

print("-------Ex5-------")

FNPI = ["3", "2", "+", "13", "*"]
operande = []

for i in range(2):
    operande.append(FNPI.pop(0))

print("Premières opérandes:", operande)

if FNPI[0] == "+":
    res1 = int(operande[0]) + int(operande[1])
elif FNPI[0] == "-":
    res1 = int(operande[0]) - int(operande[1])
elif FNPI[0] == "*":
    res1 = int(operande[0]) * int(operande[1])
elif FNPI[0] == "/":
    res1 = int(operande[0]) / int(operande[1])
else:
    print("opération invalide!")

print("Résultat de la première opération:", res1)

FNPI = ["3", "2", "+", "13", "*"]
operande2 = []

if len(FNPI) > 3 and len(FNPI) < 6:
    for i in range(3):
        FNPI.pop(0)
    
    operande2.append(FNPI.pop(0))
    operande2.append(res1)
    res2 = ""

    print("Deuxièmes opérandes:", operande2)

    if FNPI[0] == "+":
        res2 = int(operande2[0]) + int(operande2[1])
    elif FNPI[0] == "-":
        res2 = int(operande2[0]) - int(operande2[1])
    elif FNPI[0] == "*":
        res2 = int(operande2[0]) * int(operande2[1])
    elif FNPI[0] == "/":
        res2 = int(operande2[0]) / int(operande2[1])
    else:
        print("opération invalide!")

    print("Résultat de la deuxième opération:", res2)
else:
    print("expression trop longue!")