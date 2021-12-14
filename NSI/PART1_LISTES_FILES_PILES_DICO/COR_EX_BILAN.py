def creer_pile():
    pile=[]
    return pile

def empiler(p, x):
    p.append(x)

def depiler(p):
    element=p[len(p)-1]
    p.pop()
    return element

def est_vide(p):
    if len(p)!=0:
        return False
    else:
        return True

def verifier_parentheses(s):
    p=creer_pile()
    for i in range(len(s)):
        if s[i]=='(':
            empiler(p,i)
        else:
            if est_vide(p):
                return False
            else:
                j=depiler(p)
                print((j,i))
    return est_vide(p)

print(verifier_parentheses('(()())'))
