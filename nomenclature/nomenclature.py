from datetime import date
import sys
sys.path.append("/var/www/html/projets/bureau-laurent-quancard/gestion-des-offres/gestion_tarifs_automatises/Tarifs/batchs")
import requetes_blq_test as req

sys.path.append("/var/www/html/ressources/nomenclature/appellations")
import recuperation_appellations as ra

# sys.path.append("/var/www/html/ressources/nomenclature/domainesVins")
# import traitement_domaines_vins as tvm

###
#   ATTENTION NE PAS LANCER CE FICHIER DIRECTEMENT !!! 
#   Si vous voulez le faire liser le fichier "nomenclature_test.py"
###

dictionnaire_nomenclature = {"VGC": "Vins Grands Crus", "FILIPS": "Filips Wine", "BOUET": "MAISON B"}

tab_conditionnement = ["NA", "UNITE", "CBO1", "CBO1DE", "CBO1G", "CBN1", "CCBO6", "CCBO12", "Cof", "CF3", "CF6", "CF1", "COLLEC", "GIBO1", "CC100", "CC", "CBO12", "CBO12DE", "CBO12PLA", "CBN", "CBN12", "C12D", "CC12DE", "CCN12",
"CBO16", "CBO2", "CBN2", "CBO24DE", "CC24", "CBO3", "CBN3", "CBO4", "CB4MAG", "CBN4", "CBO5", "CC5", "CBO6", "CBO6DE", "CBO6CLA", "CBO6PLA", "CBN6", "CC6COU", "CC6DEB", "CC6DES", "CC6PLA", "CCN6", "BOX", "CC7", "CBO8",
"CC1", "ETUI1", "CC2", "CC3", "CC4", "CC6", "CBO9", "CBO", "CC12", "CB1", "CB3", "CB6", "CB12", "CBO24"]

tab_format_bouteille = ["NA", "BO", "DE", "CL", "L", "MG", "DM", "JE", "IM", "RE", "SA", "BA", "NA", "ME", "BABY", "NON RECONNU", "JEROCH", "MJ", "MAT", "MI", "PR", "1/4", "TX", "WIT"]

tab_couleur = ["NA", "ROUGE", "BLANC", "ROSE", "MIXED"]

tab_pays_pays : list = ["NA", "FRANCE", "ANGLETERRE", "ALLEMAGNE"]
tab_pays_continent : list = ["NA", "EUROPE", "EUROPE", "EUROPE", "EUROPE"]
tab_pays : list = [tab_pays_pays, tab_pays_continent]

tab_type_partenaire : list = ["NA","DOMAINE","NEGOCIANT", "DISTRIBUTEUR"]

tab_type_tarif_type_tarif : list = ["NA", "OFFICIEL", "OFFICIEUX", "EXPORT"]
tab_type_tarif_description : list = ["NA", "tarif place visible", "tarif place invisible", "tarif non place"]
tab_type_tarif : list = [tab_type_tarif_type_tarif, tab_type_tarif_description]

tab_flux_nom : list = ["NA", "XML", "GOOGLE SHEETS", "EMAIL", "FLASH"]
tab_flux_type : list = ["NA", "FLUX", "FLUX", "COURRIER", "COURRIER"]
tab_flux : list = [tab_flux_nom, tab_flux_type]

tab_profil_profil : list = ["NA", "MILIMA", "ANGWIN_HEBDO", "CUVFAU", "MAISOB"]
tab_profil_chemin : list = ["NA", "MILLESIMA", "ANGWIN_HEBDO", "CUVFAU", "MAISOB"]
tab_profil_flux : list = ["NA", "http://admin.millesima.fr/media/productsfeedpick/fr.xml", "https://www.vinsetmillesimes.com/gmerchantcenterpro87f0116d88fbb4ac32bbbe5f4fd44afc.fr.EUR.shop1.product.xml", "1dWHRCDE99uXQ1IbTZNm1XYLzRwMwLyg3TcJzmzINV-M", "C1aqe6HRgndilOFTEmuSncSGNly7VesKExNjIouGXW0UM"]
tab_profil_type_tarif_id : list = [1, 2, 2, 2, 2]
tab_profil_flux_id : list = [1, 2, 2, 3, 3]
tab_profil_partenaire_id : list = [1, 2, 3, 4, 5]
tab_profil : list = [tab_profil_profil, tab_profil_chemin, tab_profil_flux, tab_profil_type_tarif_id, tab_profil_flux_id, tab_profil_partenaire_id]

tab_partenaire_pays_id : list = [ 1, 2, 2, 2, 2 ]
tab_partenaire_type_partenaire_id : list = [ 1, 3, 3, 3, 3 ]
# retrouver les vrais noms !!
tab_partenaire_nom : list = ["NA", "MILLESIMA", "ANGWIN_HEBDO", "CUVFAU", "MAISOB"]
tab_partenaire_code : list = ["", "", "", "", ""]
tab_partenaire : list = [tab_partenaire_pays_id, tab_partenaire_type_partenaire_id, tab_partenaire_nom, tab_partenaire_code]

base_blq_str : str = "bd_blq"

# millesime : (int, "", "")
tuple_colonnes_millesime : tuple = ("millesime", "etiquette", "degre")

stock_offres_str : str = "stock_offres"
tarif_str : str = "tarif"
conditionnement_str : str = "conditionnement"
format_bouteille_str : str = "format_bouteille"
millesime_str : str = "millesime"
vin_str : str = "vin"
couleur_vin_str : str = "couleur_vin"
appellation_str : str = "appellation"
domaine_str : str = "domaine"

pays_str : str = "pays"
type_partenaire_str : str = "type_partenaire"
partenaire_str : str = "partenaire"
profil_str : str = "profil"
flux_str : str = "flux"
type_tarif_str : str = "type_tarif"

# Fonction permettant de réinitialiser une table où seul des données d'une colonne doivent être insérer
def reinitialisation_table_une_colonne(nom_table : str, nom_colonne : str, tab_valeurs : list):
    
    req.reinitialisation_global([nom_table])

    for valeur in tab_valeurs:

        valeur : str = str(valeur)

        print("valeur : "+ str(valeur)) 

        if(valeur.isnumeric()):
            requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne + """) VALUES (""" + valeur + """);"""
        else:
            requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne + """) VALUES ('""" + valeur + """');"""

        req.envoie_requete_sans_retour(requete)

def enregistrement_millesime():

    req.reinitialisation_global(["millesime"])

    date_max : int = 2022
    date_min : int = 1800

    requete = f"""INSERT INTO millesime(millesime) VALUES (0);"""
    req.envoie_requete_sans_retour(requete)

    for valeur in range(date_min, date_max + 1):

        requete = f"""INSERT INTO millesime(millesime) VALUES ('{valeur}');"""

        req.envoie_requete_sans_retour(requete)  
        # tuple_valeurs : tuple = (valeur, 'etiquette', 'degre')
        # req.insertion_simple("millesime", tuple_colonnes_millesime, tuple_valeurs)

def suppression_des_donnees_pour_initialisation():

    table_a_vider : list = ['tarif', 'stock_offres']

    req.supprimer_tout(table_a_vider)

def main():
    # Commenter les méthodes après les avoir utilisées !!
    print()

    # suppression des enregistrements des stocks et tarifs afin de modifier les autres tables qui leur sont liées
    tab_table = [profil_str, tarif_str, type_tarif_str, stock_offres_str]
    req.reinitialisation_global(tab_table)

    # contionnement
    reinitialisation_table_une_colonne(conditionnement_str, "conditionnement", tab_conditionnement)

    # format bouteille
    reinitialisation_table_une_colonne(format_bouteille_str, "format_bouteille", tab_format_bouteille)

    # millesime
    date_max : int = 2022
    date_min : int = 1800

    tab_millesime = range(date_min, date_max + 1)
    reinitialisation_table_une_colonne(millesime_str, "millesime", tab_millesime)

    # suppression des enregistrements des vins afin de modifier les autres tables qui leur sont liées
    req.reinitialisation_global([vin_str])

    # couleur
    reinitialisation_table_une_colonne(couleur_vin_str, "couleur", tab_couleur)

    # appellation
    reinitialisation_table_une_colonne(appellation_str, "appellation", ra.recuperation_appellations())

    # domaine-vin A REVOIR !!!
    req.reinitialisation_global([domaine_str])

    # suppression des enregistrements des profils afin de modifier les autres tables qui leur sont liées
    # req.reinitialisation_global([profil_str])

    # flux
    req.reinitialisation_global([flux_str])

    nom_table = "flux"
    nom_colonne1 = "nom"
    nom_colonne2 = "type"

    i : int = 0

    for i in range(0, len(tab_flux[0])):

        requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + tab_flux[0][i] + """','""" + tab_flux[1][i] + """');"""

        req.envoie_requete_sans_retour(requete)

    # type_tarif
    # req.reinitialisation_global([type_tarif_str])

    nom_table = "type_tarif"
    nom_colonne1 = "type_tarif"
    nom_colonne2 = "description"

    i : int = 0

    for i in range(0, len(tab_type_tarif[0])):

        requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + tab_type_tarif[0][i] + """','""" + tab_type_tarif[1][i] + """');"""

        req.envoie_requete_sans_retour(requete)

    # suppression des enregistrements des partenaires afin de modifier les autres tables qui leur sont liées
    req.reinitialisation_global([partenaire_str])

    # pays
    req.reinitialisation_global([pays_str])

    nom_table = "pays"
    nom_colonne1 = "nom"
    nom_colonne2 = "continent"

    i : int = 0

    for i in range(0, len(tab_pays[0])):

        requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + ""","""+ nom_colonne2 +""") VALUES ('""" + tab_pays[0][i] + """','""" + tab_pays[1][i] + """');"""

        req.envoie_requete_sans_retour(requete)

    # type_partenaire
    reinitialisation_table_une_colonne(type_partenaire_str, "type", tab_type_partenaire)
    
    # partenaire
    nom_table = "partenaire"
    nom_colonne1 = "pays_id"
    nom_colonne2 = "type_partenaire_id"
    nom_colonne3 = "nom"
    nom_colonne4 = "partenaire_code"
    
    nom_tab = ["MILLESIMA", "ANGEL WINE", "CUVELIER FAUVARQUE", "MAISON B  "]

    i = 0

    print("len(tab_partenaire) : " + str(len(tab_partenaire)))
    print("nom_table : " + nom_table)
    print("nom_colonne1 : " + nom_colonne1)
    print("nom_colonne2 : " + nom_colonne2)
    print("nom_colonne3 : " + nom_colonne3)
    print("nom_colonne4 : " + nom_colonne4)

    for i in range(0, len(tab_partenaire_nom)):

        print("tab_partenaire[0][i] : " + str(tab_partenaire[0][i]))
        print("tab_partenaire[1][i] : " + str(tab_partenaire[1][i]))
        print("tab_partenaire[2][i] : " + str(tab_partenaire[2][i]))
        print("tab_partenaire[2][i] : " + str(tab_partenaire[3][i]))

        # pays_id : int = tab_pays[0].index()

        tuple_valeurs : tuple = (tab_partenaire[0][i], tab_partenaire[1][i], tab_partenaire[2][i], tab_partenaire[3][i])

        requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + """,""" + nom_colonne2 + """,""" + nom_colonne3 + """,""" + nom_colonne4 + """) 
        VALUES (%s, %s, %s, %s);"""

        req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs)

    # profil : a revoir id à trouver dans les tables
    nom_table = "profil"
    nom_colonne1 = "profil"
    nom_colonne2 = "chemin"
    nom_colonne3 = "flux"

    nom_colonne4 = "type_tarif_id"
    nom_colonne5 = "flux_id"
    nom_colonne6 = "partenaire_id"

    i : int = 0

    for i in range(0, len(tab_profil_profil)):

        print(tab_profil[0])

        print("tab_profil[0][i] : " + str(tab_profil[0][i]))
        print("tab_profil[1][i] : " + str(tab_profil[1][i]))
        print("tab_profil[2][i] : " + str(tab_profil[2][i]))
        print("tab_profil[3][i] : " + str(tab_profil[3][i]))
        print("tab_profil[4][i] : " + str(tab_profil[4][i]))
        print("tab_profil[5][i] : " + str(tab_profil[5][i]))

        tuple_valeurs : tuple = (tab_profil[0][i],tab_profil[1][i],tab_profil[2][i], tab_profil[3][i],tab_profil[4][i],tab_profil[5][i])

        requete = f"""INSERT INTO """ + nom_table + """(""" + nom_colonne1 + """,""" + nom_colonne2 + """,""" + nom_colonne3 + """,""" + nom_colonne4 + """,""" + nom_colonne5 + """,""" + nom_colonne6 + """) 
        VALUES (%s, %s, %s, %s, %s, %s);"""

        req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs)

    # domaine-vin

    # tvm.traitement_vins()

    # stock_offres ??

    # tarif ??



