#Exercice 4
F1=["A","B","C","D","E"]        #On défini la file F1
P2=[]        #On initialise la pile P2
F1.reverse()         #On inverse la file 1
P1=F1    #On ajoute la file F1 a P1
print("la pile 1 vaut ", P1) #On affiche P1
for i in range(5) :        #On crée une boucle
    N=P1.pop()       #On enlève le dernier element de la liste et on l'ajoute a N
    print(N)    #On affiche N
    P2.append(N)        #On ajoute la valeur N a P2
print("la pile 2 vaut ",P2) #On affiche P2




