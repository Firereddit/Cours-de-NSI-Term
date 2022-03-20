#definir un dictionnaire:
print("""definir un dictionnaire:

""")
mon_dictionnaire = {"bateau": "flotent", "vélo": "roule"}

#acceder a une valeur dans mon dictionnaire:
print("""acceder a une valeur dans mon dictionnaire:

""")
print(mon_dictionnaire["bateau"])

#construire une entrée dans un dictionnaire:
print("""construire une entrée dans un dictionnaire:

""")
mon_dictionnaire["avion"] = "vole"
print(mon_dictionnaire)

#recuperer le type d'un dictionnaire:
print("""recuperer le type d'un dictionnaire:

""")
print(type(mon_dictionnaire))

#parcourir un dictionnaire:
print("""parcourir un dictionnaire:

""")
nb_de_roues = {"voiture": 4, "vélo": 2, "tricycle": 3}

for i in nb_de_roues.items():
    print(i)

    #ou
print(mon_dictionnaire.items())

#récuperer les valeurs:
for i in mon_dictionnaire.values():
    print(i)

    #ou
print(mon_dictionnaire.values())

#récupéreré les clefs:
for i in mon_dictionnaire.keys():
    print(i)
    
    #ou
print(mon_dictionnaire.keys())

#récupérer des valeurs grâce aux clefs:
print (mon_dictionnaire.get("bateau"))

#trier les valeurs du dictionnaire:
mon_dictionnaire_a_trier = {"a": 5, "b": 3, "c": 9, "d": 8}
print(sorted(mon_dictionnaire_a_trier))

    #même chose mais inversé:
print(sorted(mon_dictionnaire_a_trier, reverse=True))

#ajouter une valeure au dictionnaire:
mon_dictionnaire_a_trier['e'] = 12
print(mon_dictionnaire_a_trier)

#modifier une valeure correspondant à une clef:
mon_dictionnaire_a_trier['e'] = 24

#supprimer un item du dictionnaire:
del(mon_dictionnaire_a_trier['e'])
print(mon_dictionnaire_a_trier)

#transformer un dictionnaire en liste (seulement les clefs):
print(list(mon_dictionnaire_a_trier))

#classer les items par nombre (pour correspondre aux listes):
for i in mon_dictionnaire_a_trier:
    print(list(enumerate(mon_dictionnaire_a_trier)))

#autre exemple:
print("""autre exemple:

""")
for cle, valeur in nb_de_roues.items():
    print("l'élément de clé", cle, "vaut", valeur)