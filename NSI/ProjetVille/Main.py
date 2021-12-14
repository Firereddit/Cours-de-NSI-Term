import turtle as t
import random as r

t.speed("fastest")
#t.ht()
t.pensize(1)

nblotissements = 3

def espace(size=0):
    t.penup()
    t.forward(size)
    t.pendown()

def diag(length=0, height=0):
    t.penup()
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.pendown()

def couleur_aleatoire():
    color = ["#"+''.join([r.choice('0123456789ABCDEF') for j in range(6)])]
    return color

def toit_plat(color="#000000"):
    t.color(color)
    t.pensize(10)
    t.penup()
    diag(-10,0)
    t.pendown()
    t.forward(160)
    t.pensize(1)

def toit_triangle(color="#000000"):
    t.color(color)
    t.pensize(1)
    t.penup()
    diag(-10,0)
    t.pendown()
    t.begin_fill()
    t.forward(160)
    t.left(149)
    t.forward(90)
    t.left(60)
    t.forward(95)
    t.end_fill()
    t.setheading(0)
    espace(160)
    t.pensize(1)

def fenetres(length=30, height=30, color="#FFFFFF"):
    t.color("#000000", color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def porte_fenetre(length=30, height=45, color="#FFFFFF"):
    t.color("#000000", color)
    t.begin_fill()
    fenetres(length, height, color)
    #faire le balcon (le morceau de bois de merde là)
    # merci diegooo ^^

def porte1(length=30, height=40, radius=15, color="#000000"):
    t.color("#000000", color)
    t.begin_fill()
    t.setheading(-90)
    t.forward(5)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.setheading(0)
    t.begin_fill()
    for i in range(2):
        t.penup()
        t.forward(length)
        t.right(90)
        t.pendown()
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.forward(5)
    t.setheading(0)
    t.pendown()

def porte2(length=30, height=45, color="#000000"):
    fenetres(length, height, color)

def etages(length=140,height=60, color="#FFFFFF"):
    t.color("#000000", color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    diag((140-90)/4, 15)
    for i in range(3):
        e = r.randint(1, 2)
        t.setheading(0)
        if e == 1:
            fenetres()
        else:
            porte_fenetre()
        espace(50/4)
        espace(30)

def res_de_chausse(length=140, height=60, color="#FFFFFF"):
    t.color("#000000", color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    diag((140-90)/4, 15)
    uneporte = False
    for i in range(3):
        if uneporte == False:
            e = r.randint(1, 2)
        else:
            e = 1
        t.setheading(0)
        if i == 2 and uneporte == False:
            e = 2
        if e == 1:
            fenetres()
        else:
            e = r.randint(1,2)
            if e ==1:
                porte1(color=couleur_aleatoire())
            else:
                porte2(color=couleur_aleatoire())
            uneporte = True
        
        espace(50/4)
        espace(30)

def etage_sup():
    t.penup()
    t.setheading(90)
    t.forward(60)
    t.setheading(0)
    t.pendown()


def batiment(nbetages=r.randint(0,4)):
    global nombre_etage
    nombre_etage = nbetages
    couleur_batiment=couleur_aleatoire()
    res_de_chausse(color=couleur_batiment)
    for i in range(nbetages):
        t.penup()
        t.forward(-140)
        t.setheading(90)
        t.forward(15)
        t.setheading(0)
        t.pendown
        etage_sup()
        etages(color=couleur_batiment)
    t.penup()
    t.forward(-140)
    t.setheading(90)
    t.forward(15)
    t.setheading(0)
    t.pendown
    e = r.randint(0,1)
    if e == 1:
            toit_plat()
    else:
        toit_triangle()
    return nombre_etage

def lotissement():
    for i in range(4):
        batiment(nbetages=r.randint(0,4))
        t.penup()
        t.setheading(-90)
        t.forward(60*nombre_etage)
        t.setheading(0)
        t.forward(25)
        t.pendown()
def sol():
    espace(-((160*4)+45))
    t.color("#784212")
    t.setheading(-90)
    espace(60)
    t.pensize(10)
    t.setheading(0)
    t.forward((160*4)+40)
    t.color("#000000")
    espace(-((140*4)+35))
    t.setheading(90)
    espace(65)
    t.setheading(0)
    t.pensize(1)
    espace(-80)

def sol_centre():
    espace((-((160*4)+45))/2)
    t.color("#784212")
    t.setheading(-90)
    espace(60)
    t.pensize(10)
    t.setheading(0)
    t.forward((160*4)+40)
    t.color("#000000")
    espace(-((140*4)+35))
    t.setheading(90)
    espace(65)
    t.setheading(0)
    t.pensize(1)
    espace(-80)

def ville(nblotissements=3):
    for i in range(nblotissements):
        if i >1:
            t.penup()
            t.goto(0,0)
            t.setheading(-90)
            espace(360)
            t.setheading(0)
            t.pendown()
            sol_centre()
            lotissement()
            t.setheading(-90)
            espace(5)
            t.setheading(0)
            espace(((160*4)+45))
        else:
            sol()
            lotissement()
            t.setheading(-90)
            espace(5)
            t.setheading(0)
            espace(((160*4)+45))
        



ville()

t.exitonclick()
