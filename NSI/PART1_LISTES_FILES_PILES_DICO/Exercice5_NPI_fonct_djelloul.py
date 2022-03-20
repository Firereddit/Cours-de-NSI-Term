NPI_P1=[3, 2, '+', 13, '*']
NPI_P1.reverse()
print(NPI_P1)
A=NPI_P1.pop(4)
B=NPI_P1.pop(3)
D=NPI_P1.pop(2)
print(D)

if D=="+":
    C=A+B
elif D=="-":
    C=A-B
elif D=="*":
    C=A*B
elif D=="/":
    C=A/B
else:
    print("Error !")

print(NPI_P1)
NPI_P1.append(C)
E=NPI_P1.pop(1)
G=NPI_P1.pop(0)
if G == '*':
    F=C*E
elif G == '/':
    F=C/E
elif D=="+":
    F=C+E
elif D=="-":
    F=C-E
else:
    print("Error !")

NPI_P1.append(F)
print(NPI_P1)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)





