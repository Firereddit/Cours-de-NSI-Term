
f1 = ['3','2', '+','13','*']
P2=[]

for i in range(3):
    P1 = f1.pop(0)
    print (P1)
    P2.append(P1)
    print(P2)
print(f1)

if  '+' in P2 :
    P3=int(P2.pop(0))
    P4=int(P2.pop(0))
    P2=P3+P4
print ("la valeur de P2 est:", P2)

if "*" in f1:
    f2  = int(f1.pop(0))
    F3 = f2*P2

print('la valeur de F3 est :', F3)
