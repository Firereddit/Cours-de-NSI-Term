#fonctions de base pour une file
def creer_file():
    file=[]
    return file

def enfiler(f,x):
    f.append(x)

def defiler(f):
    return f.pop(0)

def est_vide(f):
    if len(f)!=0:
        return False
    else:
        return True

file_test=creer_file()
enfiler(file_test,'C')
enfiler(file_test,'B')
enfiler(file_test,'A')
print(defiler(file_test))