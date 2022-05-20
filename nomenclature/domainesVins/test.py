### Test pour la récupération d'une référence par rapport à une chaine de caractère ###

# liste1 : list = ['liste1', 'Gayerie1', 'David']
# liste2 : list = ['liste2', 'Gayerie', 'David2']
liste1 : list = ['liste1', 1, 3]
liste2 : list = ['liste2', 4, 2]
liste_reference_debut : list = [liste1, liste2]

# liste3 : list = ['Gayerie1', 'David2']
liste3 : list = [1, 2]

def retour_premier_element_avec_valeur(liste_reference : list, valeur_a_tester):

    for liste in liste_reference :
        if(valeur_a_tester in liste):
            return liste[0]
    return "NA"

for valeur in liste3 :
    print("valeur : " + retour_premier_element_avec_valeur( liste_reference_debut, valeur ))

# Fonction dans Fonction_tarifs_dev
# def recup_ref_avec_valeur(liste_reference : list, valeur_a_tester):

#     for liste in liste_reference :
#         print("valeur : " + retour_premier_element_avec_valeur( liste, valeur_a_tester ))

# for valeur in liste3 :

#     # if( liste3[0] == valeur ):
#     #     continue

#     print("valeur 1 :")
#     print(valeur)

#     print("valeur : " + recup_ref_avec_valeur( liste_reference_debut, valeur ))





         