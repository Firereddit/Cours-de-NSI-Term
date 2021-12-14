from turtle import *
from random import *
global a,b,c
a = 0
b = 0
c = 0
d = 0
class ArbreBinaire:
    def __init__(self, valeur):
        self.contenu = valeur
        self.filsGauche = None
        self.filsDroit = None

    def ajoutFilsGauche(self, valeur):
        if self.filsGauche == None :
            self.filsGauche = ArbreBinaire(valeur)
        else :
            self.filsGauche.ajoutFilsGauche(valeur)

    def ajoutFilsDroit(self, valeur):
        if self.filsDroit == None :
            self.filsDroit = ArbreBinaire(valeur)
        else :
            self.filsDroit.ajoutFilsDroit(valeur)

    def ajoutContenu(self, valeur):
        global NfilsGauche
        global NfilsDroit
        if valeur != self.contenu:
            if valeur < self.contenu:
                if self.filsGauche == None:
                    self.filsGauche = ArbreBinaire(valeur)
                else:
                    self.filsGauche.ajoutContenu(valeur)
            else:
                if self.filsDroit == None:
                    self.filsDroit = ArbreBinaire(valeur)
                else:
                    self.filsDroit.ajoutContenu(valeur)

    def __str__(self):
        return(f"[ Contenu : {self.contenu} / Fils Gauche : {self.filsGauche} / Fils Droit : {self.filsDroit} ] ")

arbreWiki = ArbreBinaire(8)
for i in range(1000):
    arbreWiki.ajoutContenu(randint(0,500))



def initDessin():
    penup()
    sety(300)
    seth(300)
    pendown()
    speed("fastest")
    width(5)
    bgcolor("black")

def dessineNoeud():
    global a,b,c,d
    colormode(255)
    if d == 0:
        if a < 255:
            a += 1
            b += 1
            c += 1
        else: d = 1
    else:
        if d == 1:
            a -= 1
            b -= 1
            c -= 1
    color(a, b, c)
    width(4)

def DessinParcoursProfondeurPostFixe(arbre):
    if (arbre.filsGauche != None):
        right(30)
        forward(50)
        DessinParcoursProfondeurPostFixe(arbre.filsGauche)
        backward(50)
        left(30)
    if (arbre.filsDroit != None):
        left(30)
        forward(50)
        DessinParcoursProfondeurPostFixe(arbre.filsDroit)
        backward(50)
        right(30)
    dessineNoeud()                                 # PostFixe donc on traite "après les fils"

initDessin()                                    # On ré-initialise le dessin
DessinParcoursProfondeurPostFixe(arbreWiki)      # On dessine

mainloop() #La fenêtre ne se ferme pas aprs l'éxécution du programme