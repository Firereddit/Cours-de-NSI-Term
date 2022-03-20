def est_impair(a):
    """la fonction est_impaire qui prends come paramètre a renvoie True si le nombre entré en parapètre est Impaire False sinon"""
    if a %2 != 0:
        return True
    else:
        return False

assert est_impair(10) == False
assert est_impair(11) == True

###Turtle

import turtle as t
def trianglehaut(lenght, c="#000000"):
    """cette fonction va dessiner un triangle de longeur 'lenght' vers le haut et de couleur définie par l'utilisater ou blanche sinon"""
    t.color(c)
    for i in range(3):
        t.forward(lenght)
        t.left(360/3)

def trianglebas(lenght, c="#000000"):
    """cette fonction va dessiner un triangle de longeur 'lenght' vers le bas et de couleur définie par l'utilisater ou blanche sinon"""
    t.color(c)
    for i in range(3):
        t.forward(lenght)
        t.right(360/3)

def square(lenght, c="#000000"):
    """cette fonction va dessiner un carre de longeur 'lenght' et de couleur définie par l'utilisater ou blanche sinon"""
    t.color(c)
    for i in range(4):
        t.forward(lenght)
        t.right(360/4)

def rectangle(lenght, width, c="#000000"):
    """cette fonction va dessiner un rectangle de longeur 'lenght', de largeur 'width' et de couleur définie par l'utilisater ou blanche sinon"""
    t.color(c)
    for i in range(2):
        t.forward(lenght)
        t.right(360/4)
        t.forward(width)
        t.right(360/4)

def polygone(lenght, sides, c="#000000"):
    """cette fonction va dessiner un rectangle de longeur 'lenght', de largeur 'width' et de couleur définie par l'utilisater ou blanche sinon"""
    t.color(c)
    for i in range(sides):
        t.forward(lenght)
        t.right(360/sides)

def espace(lenght, c="#000000"):
    """cette fonction va creer un espace de longeur 'lenght'"""
    t.penup()
    t.forward(lenght)
    t.pendown()

