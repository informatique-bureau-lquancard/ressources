import nomenclature as nom

import sys

sys.path.append("/var/www/html/projets/bureau-laurent-quancard/gestion-des-offres/gestion_tarifs_automatises/Tarifs/batchs")
import requetes_blq_test as req

sys.path.append("/var/www/html/ressources/nomenclature/appellations")
import recuperation_appellations as ra

import ressources_bd_blq.formatage_fichier_LWIN as ffl

# import domainesVins.traitement_domaines_vins as tdv

# sys.path.append("/var/www/html/ressources/nomenclature/domainesVins")
# import traitement_domaines_vins as tvm

###
#   ATTENTION NE PAS LANCER CE FICHIER DIRECTEMENT !!! 
#   Si vous voulez le faire liser le fichier "nomenclature_test.py"
#
#   Si vous voulez réinitialiser toute la base il faudra aussi lancer le traitement "traitement_domaines_vins.py"
###

# Fonction permettant de réinitialiser une table où seul des données d'une colonne doivent être insérer
def reinitialisation_table_une_colonne(nom_table : str, nom_colonne : str, tab_valeurs : list):
    
    req.reinitialisation_global([nom_table])

    for valeur in tab_valeurs:

        valeur : str = str(valeur)

        # print("valeur : "+ str(valeur)) 

        if(valeur.isnumeric()):
            requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne + """) VALUES (""" + valeur + """);"""
        else:
            requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne + """) VALUES ('""" + valeur + """');"""

        req.envoie_requete_sans_retour(requete)

def suppression_des_donnees_pour_initialisation():

    table_a_vider : list = ['tarif', 'stock_offres']

    req.supprimer_tout(table_a_vider)

def main():
    
    print("Démarrage initialisation_bd_blq")

    # Formatage du fichier LWIN
    ffl.formaterFichierLWIN()

    # # suppression des enregistrements des stocks et tarifs afin de modifier les autres tables qui leur sont liées
    # tab_table = [nom.profil_str, nom.tarif_str, nom.type_tarif_str, nom.stock_offres_str]
    # req.reinitialisation_global(tab_table)

    # # contionnement
    # reinitialisation_table_une_colonne(nom.conditionnement_str, "conditionnement", nom.tab_conditionnement)

    # # format bouteille
    # reinitialisation_table_une_colonne(nom.format_bouteille_str, "format_bouteille", nom.tab_format_bouteille)

    # # millesime
    # date_max : int = 2022
    # date_min : int = 1800

    # tab_millesime_entier = range(date_min, date_max + 1)
    # tab_millesime = list( map( str, tab_millesime_entier ) )
    # tab_millesime.insert(0, "NV")

    # reinitialisation_table_une_colonne(nom.millesime_str, "millesime", tab_millesime)

    # # suppression des enregistrements des vins afin de modifier les autres tables qui leur sont liées
    # req.reinitialisation_global([nom.vin_str])

    # # couleur
    # reinitialisation_table_une_colonne(nom.couleur_vin_str, "couleur", nom.tab_couleur)###

    # # appellation
    reinitialisation_table_une_colonne(nom.appellation_str, "appellation", ra.recuperation_appellations())

    # # domaine-vin A REVOIR !!!
    # req.reinitialisation_global([nom.domaine_str])

    # # flux
    # req.reinitialisation_global([nom.flux_str])

    # nom_table = "flux"
    # nom_colonne1 = "nom"
    # nom_colonne2 = "type"

    # i : int = 0

    # for i in range(0, len(nom.tab_flux[0])):

    #     requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + nom.tab_flux[0][i] + """','""" + nom.tab_flux[1][i] + """');"""

    #     req.envoie_requete_sans_retour(requete)

    # nom_table = "type_tarif"
    # nom_colonne1 = "type_tarif"
    # nom_colonne2 = "description"

    # i : int = 0

    # for i in range(0, len(nom.tab_type_tarif[0])):

    #     requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + nom.tab_type_tarif[0][i] + """','""" + nom.tab_type_tarif[1][i] + """');"""

    #     req.envoie_requete_sans_retour(requete)

    # # suppression des enregistrements des partenaires afin de modifier les autres tables qui leur sont liées
    # req.reinitialisation_global([nom.partenaire_str])

    # # pays
    # req.reinitialisation_global([nom.pays_str])

    # nom_table = "pays"
    # nom_colonne1 = "nom"
    # nom_colonne2 = "continent"

    # i : int = 0

    # for i in range(0, len(nom.tab_pays[0])):

    #     requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + nom.tab_pays[0][i] + """','""" + nom.tab_pays[1][i] + """');"""

    #     req.envoie_requete_sans_retour(requete)

    # # type_partenaire
    # reinitialisation_table_une_colonne(nom.type_partenaire_str, "type", nom.tab_type_partenaire)
    
    # # partenaire
    # nom_table = "partenaire"
    # nom_colonne1 = "pays_id"
    # nom_colonne2 = "type_partenaire_id"
    # nom_colonne3 = "nom"
    # nom_colonne4 = "partenaire_code"
    
    # nom_tab = ["MILLESIMA", "ANGEL WINE", "CUVELIER FAUVARQUE", "MAISON B  "]

    # i = 0

    # # print("len(tab_partenaire) : " + str(len(nom.tab_partenaire)))
    # # print("nom_table : " + nom_table)
    # # print("nom_colonne1 : " + nom_colonne1)
    # # print("nom_colonne2 : " + nom_colonne2)
    # # print("nom_colonne3 : " + nom_colonne3)
    # # print("nom_colonne4 : " + nom_colonne4)

    # for i in range(0, len(nom.tab_partenaire_nom)):

    #     # print("tab_partenaire[0][i] : " + str(nom.tab_partenaire[0][i]))
    #     # print("tab_partenaire[1][i] : " + str(nom.tab_partenaire[1][i]))
    #     # print("tab_partenaire[2][i] : " + str(nom.tab_partenaire[2][i]))
    #     # print("tab_partenaire[2][i] : " + str(nom.tab_partenaire[3][i]))

    #     # pays_id : int = tab_pays[0].index()

    #     tuple_valeurs : tuple = (nom.tab_partenaire[0][i], nom.tab_partenaire[1][i], nom.tab_partenaire[2][i], nom.tab_partenaire[3][i])

    #     requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + """,""" + nom_colonne2 + """,""" + nom_colonne3 + """,""" + nom_colonne4 + """) 
    #     VALUES (%s, %s, %s, %s);"""

    #     req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs)

    # # profil : a revoir id à trouver dans les tables
    # nom_table = "profil"
    # nom_colonne1 = "profil"
    # nom_colonne2 = "chemin"
    # nom_colonne3 = "flux"

    # nom_colonne4 = "type_tarif_id"
    # nom_colonne5 = "flux_id"
    # nom_colonne6 = "partenaire_id"

    # i : int = 0

    # for i in range(0, len(nom.tab_profil_profil)):

    #     # print(nom.tab_profil[0])

    #     # print("tab_profil[0][i] : " + str(nom.tab_profil[0][i]))
    #     # print("tab_profil[1][i] : " + str(nom.tab_profil[1][i]))
    #     # print("tab_profil[2][i] : " + str(nom.tab_profil[2][i]))
    #     # print("tab_profil[3][i] : " + str(nom.tab_profil[3][i]))
    #     # print("tab_profil[4][i] : " + str(nom.tab_profil[4][i]))
    #     # print("tab_profil[5][i] : " + str(nom.tab_profil[5][i]))

    #     tuple_valeurs : tuple = (nom.tab_profil[0][i],nom.tab_profil[1][i],nom.tab_profil[2][i], nom.tab_profil[3][i], nom.tab_profil[4][i], nom.tab_profil[5][i])

    #     requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + """,""" + nom_colonne2 + """,""" + nom_colonne3 + """,""" + nom_colonne4 + """,""" + nom_colonne5 + """,""" + nom_colonne6 + """) 
    #     VALUES (%s, %s, %s, %s, %s, %s);"""

    #     req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs)

    # domaine-vin
    # tdv.recuperationVins()
