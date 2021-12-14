p = ['(', '(', ')', ')', '(', ')']          #Définition de la liste p

def ParenthesesReturn(p):           #définition de la fonction ParentheseReturn
    PileParOuv = []         #Initialisation des listes nécéssaires
    PileParFer = []
    PileCouples = []
    lgt = len(p)            #définition de la variable lgt pour pouvoir la comparer en suivant
    if len(p) == 0 or not p or lgt/2 != lgt//2:         #condition vérifiant si la liste est valide et utilisable 
        print (f'Votre chaine de carectère est vide, veuillez en entrer une valide')            #renvoi de l'erreur
        ParenthesesReturn()         #Retour au debut de la fonction 

    else:           #si la condition vue au dessus n'est pas vérifiée, alors
        for i in range (len(p)):            #boucle s'executant autant de fois qu'il y a d'éléments dans la liste p
            if p[i] == '(':         #condition vérifiant si, en position i, la liste p contient une parenthese ouverte
                PileParOuv.append(i)            #On ajoute l'index de la parenthese ouverts à PileParOuv
            elif p[i] == ')':           #si la parenthese n'est pas ouverte, alors on la considère comme fermée
                PileParFer.append(i)            #On ajoute l'index de la parenthese fermée à PileParFer
                PileCouples.append(PileParOuv.pop())            #on ajoute à la fin de PileCouples la dernière valeure de PileParOuv, ce qui correspond à la derniere parenthese ouverte
                PileCouples.append(PileParFer.pop(0))           #on ajoute à la fin de PileCouples la dernière valeure de PileParFer, ce qui correspond à la derniere parenthese fermée
                print(PileCouples)          #on renvoie PileCouples dans le terminal 
                PileCouples = []            #on réinitialise pile PileCouples pour avoir des couples fixes


ParenthesesReturn(p)            #on appelle la fonction pour executer la fonction






    









