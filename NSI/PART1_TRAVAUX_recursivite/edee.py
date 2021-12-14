#n = 4

#def fonction(n):
 #   if n>0:
 #       print(n)
#
 #       fonction(n-1)

#def fonction_bis(n):
#    if n>0:

#        fonction_bis(n-1)

#    print(n)

#_________________________________________________________________________________________________________________________________________






# À faire vous-même 1

def fctA():
    ''' definie la fonction fctA'''
    print ("Début fonction fctA") #affiche "Début fonction fctA" dans la console
    i=0 # i a pour valeur 0
    while i<5: # tant que i est inferieur à 0
        print(f"fctA {i}") # afficher la valeur de i
        i = i + 1 # ajouter 1 à i
    print ("Fin fonction fctA") # afficher "Fin fonction fctA"

def fctB():
    '''definie la fonction  fctB '''
    print ("Début fonction fctB") # afficher "Début fonction fctB"
    i=0 # i a pour valeur 0
    while i<5: # tant que i est inferieur à 0
        if i==3: # si i est égale à 3
            fctA() # Appelle  la fonction A
            print("Retour à la fonction fctB") # afficher "Retour à la fonction fctB"
        print(f"fctB {i}") # sinon afficher la valeur de i
        i = i + 1 # ajouter 1 à i
    print ("Fin fonction fctB") # afficher "Fin fonction fctB"

fctB() # appelle la fonction B




# À faire vous-même 2

def fctA_():
    ''' definie la fonction A '''
    print ("Hello") # Afficher Hello
    fctA_() # appelle la fonction fctA
#fctA_() # appelle la fonction fctA



#À faire vous-même 3


def fonct(n):
    ''' definie la fonction fonct'''
    if n>0: # si n est supperieur à 0
        fonct(n-1) # Appelle de la fonction fonct et Soustraire 1 à n
    print(n) # afficher n

fonct(3) # appelle la fonction, ou n a pour valeur 3



# À faire vous-même 4

def fact(n) :
    '''definie la fonction fact '''
    if n > 0 : # si n est supperieur à 0
        return n*fact(n-1) # multiplier n fois n - 1
    else : # sinon
        return 1 # afficher 1
t=(fact(5))


print(t)




# À faire vous-même 5


nterms = int(input("combien de termes? "))

# first two terms
n1, n2 = 0, 1
count = 0

# verifier si le nombre de terme est valide
if nterms <= 0:
   print("Please enter a positive integer")
# si il y a seulment un termes, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1




#À faire vous-même 7

# triangle
import turtle as t
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)







#À faire vous-même 9


import turtle as t

def koch(longueur, n):
    '''definie la fonction koch'''
    if n == 0:# si n est égale à zero
        t.forward(longueur) # avancer de longueur
    else: # sinon
        koch(longueur/3, n-1) # appelle la fonction koch tout en divisant la longueur par 3 et retirer 1 a n
        t.left(60)   # tourner à gauche de 60 degrés
        koch(longueur/3, n-1)  # appelle la fonction koch tout en divisant la longueur par 3 et retirer 1 a n
        t.right(120) # tourner à droite de 120 degrés
        koch(longueur/3, n-1) #appelle la fonction koch tout en divisant la longueur par 3 et retirer 1 a n
        t.left(60) # tourner à gauche de 60 degrés
        koch(longueur/3, n-1)#appelle la fonction koch tout en divisant la longueur par 3 et retirer 1 a n

def flocon(taille, etape):
    ''' definie la fonction flocon '''
    koch(taille, etape) # appelle la fonction koch en utilisant la taille et etape
    t.right(120) # tourner à droiute de 120 degrés
    koch(taille, etape) # appelle la fonction koch en utilisant la taille et etape
    t.right(120) # tourner à droiute de 120 degrés
    koch(taille, etape)  # appelle la fonction koch en utilisant la taille et etape

flocon(100, 3) # appelle la fonction floncon










