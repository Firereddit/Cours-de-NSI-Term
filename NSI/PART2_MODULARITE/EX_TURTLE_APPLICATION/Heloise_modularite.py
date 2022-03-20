
# EXERCICE 1
def est_impair(a):
    ''' cette fonction va renvoyer faux si a est pair et vrai si a est impair'''
    if a%2 == 1 :
        print("est impair")
        return True

    else :
        print("est pair")
        return False

assert est_impair(3) == True
assert est_impair(2) == False

est_impair(4)






# EXERCICE 2
from turtle import *

ht() # masque la fléche
bgcolor('black')#change le fond en noir
speed('slowest')#vitesse lente de déplacement du pinceau
pensize(10)#taille du pinceau


color('red')#Change la couleur du trait du pinceau en rouge

#la boucle for permet de réaliser un carré en réitérant les tracés des côtés
for i in range(4):
    forward(50)#avance de 50 pixels
    right(90)#tourne de 90 degrés car c'est l'angle correspondant à un carré

up() #lève le pinceau pour se déplacer sur la feuille
left(90)#Tourne vers la gauche de 90 degrés
forward(100)#avance de 100 pixels pour éviter de faire le triangle sur le carré
down()#descend le stylo pour écrire
color('yellow')#change la couleur du trait en jaune

#création du traingle avec une boucle for qui itére la contruction des côtés du triangle
for i in range(3):
     forward(150)
     right(120)# tourne vers la droite d'un angle de 120 degrés

up()
left(90)
forward(100)
down()
color('blue')
circle(80)#Création d'un cercle de 80 pixels de diamètre


# EXERCICE 3
color('purple')
up()
forward(-450)
right(90)
forward(-400)
left(90)
down()


for i in range(3):
    for i in range(4):
        for i in range(3):
            forward(50)
            right(120)
        forward(50)
    up()
    forward(50)
    down()



