import csv
import glob
import time
# from subprocess import CREATE_NEW_CONSOLE
from unidecode import unidecode
import openpyxl
from openpyxl import Workbook

import glob

import pandas as pd

import warnings
warnings.simplefilter("ignore")

import os

import sys
sys.path.append("/var/www/html/projets/bureau-laurent-quancard/gestion-des-offres/gestion_tarifs_automatises/Tarifs/batchs")
import requetes_blq_test as req

import nomenclature_bd_blq as nom

sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs_dev as ft

# Pour rajouter la bibliothèque numpy : python3 -m pip install numpy
# Permet d'inverser les tableaux
import numpy as np

import peuplement_de_la_base as pp

from datetime import datetime

###
#   Les ressources pour les traitements ont été récupérés depuis le site liv-ex.com
###

# dict_couleur : dict = {"NA": 1, "RED": 2, "WHITE": 3, "ROSE": 4}
tab_couleur_vin : list = req.recuperation_tab( nom.couleur_vin_str )
tab_couleur_vin_inverse : list = list(map(list, np.transpose(tab_couleur_vin)))

# dict_pays : dict = {"NA": 1, "FRANCE": 2, "ANGLETERRE": 3, "ALLEMAGNE": 4}
tab_domaine : list = []
tab_domaine_inverse : list = []

tab_appellation : list = req.recuperation_tab( nom.appellation_str )
tab_appellation_inverse : list = list(map(list, np.transpose(tab_appellation)))

liste_rouge : list = ["ROUGE", "RED"]
liste_blanc : list = ["BLANC", "WHITE"]
liste_rose : list = ["ROSE"]
liste_mixed : list = ["MIXED"]
liste_couleur : list = [liste_rouge, liste_blanc, liste_rose, liste_mixed]

nomProfil : str = 'LWINdatabase'
extensionFin_bis : str = '.xlsx'
extensionFin : str = '.csv'

dest_filename_bis = 'sortie_bis_' + nomProfil + extensionFin_bis
dest_filename = 'sortie_' + nomProfil + extensionFin

# Requête pour connaître les doublons
# SELECT nom,COUNT(*) FROM domaine GROUP BY nom HAVING COUNT(*) > 1;

rouge_str : str = "ROUGE"
blanc_str : str = "BLANC"
margaux_str : str = "MARGAUX"
pauillac_str : str = "PAUILLAC"
saint_julien_str : str = "SAINT-JULIEN"
gruaud_larose_str : str = "CHATEAU GRUAUD LAROSE"
leoville_barton_str : str = "CHATEAU LEOVILLE BARTON"
saint_emillion_grand_cru_str : str = "SAINT-EMILION GRAND CRU"
pommerol_str : str = "POMEROL"
d_issan_str : str = "CHATEAU D ISSAN"
rieussec_str : str = "CHATEAU RIEUSSEC"
sauternes_str : str = "SAUTERNES"
chateaux_margaux_str : str = "CHATEAU MARGAUX"
chateau_beychevelle_str : str = "CHATEAU BEYCHEVELLE"

# Domaines rajoutés
liste_domaines_rajoutes : list = ["CHATEAU LASCOMBES", "CHATEAU RAUZAN GASSIES", "SC DU CHATEAU LAFITE ROTHSCHILD", "CHATEAU BRANAIRE DUCRU",
"CHATEAU DUCRU BEAUCAILLOU", "CLOS DE SARPE", "CLOS L'EGLISE", "CHATEAU CANTENAC BROWN", "SCEA BOYD CANTENAC & POUGET", "CHATEAU D ISSAN"]

# Domaine a tester
domaine_d_issan : list = ["CHATEAU D ISSAN", "CHATEAU DISSAN"]

liste_domaine_a_tester : list = [domaine_d_issan]

# Vins rajoutés
vin_chateau_lascombes : list = ["chateau lascombes".upper(), "regex", "NAN", margaux_str, rouge_str]
vin_chateau_rauzan_gassies : list = ["chateau rauzan gassies".upper(), "regex", "NAN", margaux_str, rouge_str]
vin_chateau_lafite_rotchild : list = ["chateau lafite rotchild".upper(), "regex", "NAN", pauillac_str, rouge_str]
vin_chateau_branaire_ducru : list = ["chateau branaire ducru".upper(), "regex", "NAN", saint_julien_str, rouge_str]

# Vin a tester
vin_d_issan : list = ["CHATEAU D ISSAN", "CHATEAU DISSAN"]

liste_vin_a_tester : list = [vin_d_issan]

#a revoir beycheville
vin_chateau_beychevelle : list = ["chateau beychevelle".upper(), "regex", chateau_beychevelle_str, saint_julien_str, rouge_str]

# vin_chateau_saint_pierre = ["CHATEAU RAUZAN-SEGLA", "regex", 651, 319, rouge_str]
vin_chateau_talbot : list = ["chateau talbot".upper(), "regex", "NAN", saint_julien_str, rouge_str]
vin_chateau_lagrange : list = ["chateau lagrange".upper(), "regex", "NAN", saint_julien_str, rouge_str]
vin_chateau_ducru_beau_caillou : list = ["chateau ducru beau caillou".upper(), "regex", "NAN", saint_julien_str, rouge_str]
vin_chateau_gruaud_larose : list = ["vin chateau gruaud larose".upper(), "regex", gruaud_larose_str, saint_julien_str, rouge_str]
vin_chateau_leoville_barton : list = ["chateau leoville barton".upper(), "regex", leoville_barton_str, saint_julien_str, rouge_str]

# vin_chateau_prieure_lichine = ["CHATEAU RAUZAN-SEGLA", "regex", 651, 319, rouge_str]
vin_chateau_faurie_de_souchard : list = ["chateau faurie de souchard".upper(), "regex", "NAN", saint_emillion_grand_cru_str, rouge_str]
vin_chateau_clos_de_sarpe : list = ["chateau clos de sarpe".upper(), "regex", "NAN", saint_emillion_grand_cru_str, rouge_str]
vin_clos_leglise : list = ["clos leglise".upper(), "regex", "NAN", pommerol_str, rouge_str]
vin_chateau_cantenac_brown : list = ["chateau cantenac brown".upper(), "regex", "NAN", margaux_str, rouge_str]
vin_chateau_boyd_cantenac : list = ["chateau boyd cantenac".upper(), "regex", "NAN", margaux_str, rouge_str]
# Prolème décriture : dissan et d'issan 
vin_chateau_d_issan : list = ["chateau dissan".upper(), "regex", "NAN", d_issan_str, rouge_str]

vin_carmes_de_rieussec : list = ["carmes de rieussec".upper(), "regex", rieussec_str, sauternes_str, blanc_str]
vin_rauzan_segla : list = ["CHATEAU RAUZAN-SEGLA", "regex", chateaux_margaux_str, margaux_str, rouge_str]

liste_vins_rajoutes : list = [vin_rauzan_segla, vin_carmes_de_rieussec, vin_chateau_d_issan, vin_chateau_boyd_cantenac, vin_chateau_cantenac_brown, vin_clos_leglise,
vin_chateau_clos_de_sarpe, vin_chateau_faurie_de_souchard, vin_chateau_leoville_barton, vin_chateau_gruaud_larose, vin_chateau_ducru_beau_caillou, 
vin_chateau_lagrange, vin_chateau_talbot, vin_chateau_beychevelle, vin_chateau_branaire_ducru, vin_chateau_lafite_rotchild, vin_chateau_rauzan_gassies, 
vin_chateau_lascombes]

erreur_appellation = ["APPELATIONS EN ERREUR : "]

# Copier depuis nomenclature.py
def reinitialisation_global(tab_table : list):
    
    for table in tab_table:

        requete = f"""DELETE FROM {table};"""

        req.envoie_requete_sans_retour(requete)

        requete = f"""ALTER TABLE {table} AUTO_INCREMENT = 0;"""

        req.envoie_requete_sans_retour(requete)

# Même fonction que traitement_applications : trouver un emplacement
def recupIdApresInsertion(tab_inverse : list, valeur_testee, nom_table : str, nom_colonne : str, id_colonne : int):
    
    # id : int = pp.recup_val_tab_inv2(tab_inverse, id_colonne, valeur_testee)
        
    id : int = req.recuperation_indice_doublon(nom_table, nom_colonne, valeur_testee)

    # print("id 1 : " + str(id) ) 

    # print("appellation : " + valeur_testee)

    if(id != -1):
        
        return id

    # La "," est importante car sinon cela ne marche pas
    tuple_valeurs : tuple = (valeur_testee,)
    requete = f"""INSERT INTO """+ nom_table +""" ("""+ nom_colonne +""") VALUES (%s);"""
    
    req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs)

    id : int = pp.recup_val_tab_inv2(tab_inverse, id_colonne, valeur_testee)
    # print("Retour id 2 : " + str(id))

    return id

def parcourirDictionnaireRetourneId(valeur, dictionnaire):
    for valeur_dictionnaire in dictionnaire:
        if(valeur == valeur_dictionnaire):
            return dictionnaire[valeur_dictionnaire]
    return 1

def formaterFichierLWIN():

    extensionDebut : str = '.xlsx'

    # coding: utf-8
    # On load le le tarif au format xlsx
    for filename in glob.glob('*' + extensionDebut):

        wb = openpyxl.load_workbook(filename)

    # On prépare un nouveau workbook
    wb2 = Workbook()
    ws = wb2.active
    ws.title = nomProfil

    # Lecture du workbook d'origine
    sheet_list = wb.sheetnames  # on récupère le nom des onglets, pas necessaire ici.
    sheet = wb[sheet_list[0]]

    iVinAppellation : tuple = sheet['C']
    iCouleur : tuple = sheet['L']
    iProducteur : tuple = sheet['E']
    iRegion : tuple = sheet['H']
    iPays : tuple = sheet['G']

    iProducteurTitre : tuple = sheet['D']

    row_count = sheet.max_row
    column_count = sheet.max_column

    index_sortie : int = 1

    for i  in range (1, row_count):
                
        vin : str = unidecode(str(iVinAppellation[i].value)).upper()
        region : str = unidecode(str(iRegion[i].value)).upper()
        couleur : str = unidecode(str(iCouleur[i].value)).upper()

        if( vin == "DISPLAY_NAME" or region != "BORDEAUX" or couleur == "NA"):
            continue;

        producteur : str = unidecode(str(iProducteur[i].value)).upper()
        producteur_titre : str = unidecode(str(iProducteurTitre[i].value)).upper()

        if(producteur_titre != "NA") : 
            producteur = producteur_titre + " " + producteur

        pays : str = unidecode(str(iPays[i].value)).upper()

        print("  vin : " + vin + " couleur " + couleur + " producteur " + producteur + " pays " + pays + "")

        # appellation
        # Fonction Attribution des valeurs dans les bonnes colonnes pour le nouveau workbook
        c1 = ws.cell(row = index_sortie, column = 1)
        c1.value = vin

        c2 = ws.cell(row = index_sortie, column = 2)
        c2.value = couleur

        c3 = ws.cell(row = index_sortie, column = 3)
        c3.value = producteur

        c4 = ws.cell(row = index_sortie, column = 4)
        c4.value = region

        c5 = ws.cell(row = index_sortie, column = 5)
        c5.value = pays

        index_sortie += 1

    # Fonction de suppression des lignes vides d'un workbook
    # index_row = []
    # for n in range(1, ws.max_row):
    #     if ws.cell(n, 1).value is None:
    #         index_row.append(n)

    # for row_del in range(len(index_row)):
    #     ws.delete_rows(idx=index_row[row_del], amount=1)
    #     index_row = list(map(lambda k: k -1, index_row))

    # Ecriture du nouveau workbook
    wb2.save(dest_filename_bis)

    read_file = pd.read_excel(dest_filename_bis)
    read_file.to_csv(dest_filename, index = False, encoding="utf-8", sep = ';')

def insertionDomaines():

    req.reinitialisation_global([nom.domaine_str])

    wb = openpyxl.load_workbook(dest_filename_bis)

    # Lecture du workbook d'origine
    sheet_list = wb.sheetnames  # on récupère le nom des onglets, pas necessaire ici.
    sheet = wb[sheet_list[0]]

    iDomaine = sheet['C']

    row_count = sheet.max_row

    recupIdApresInsertion(tab_domaine_inverse, "NA", nom.domaine_str, "nom", 1)

    # for i  in range (1, 100):

    domaine_id : int = -1

    for domaine_valeur  in liste_domaines_rajoutes:
    
        domaine : str = domaine_valeur.replace("'", " ")

        print("domaine : " + domaine)

        if( (len(domaine) == 0) or (domaine == "NA") or (domaine == "CHATEAU CHATEAU")):
            print("continue 1 ")
            continue

        # Insérer les lignes de domaines
        # Domaine
        domaine_id = recupIdApresInsertion(tab_domaine_inverse, domaine, nom.domaine_str, "nom", 1)

    # Ne fonctionne pas !!
    # for i  in range (1, row_count):
    #     domaine : str = (iDomaine[i].value).replace("'", " ")
    #     if( (len(domaine) == 0) or (domaine == "NA") or (domaine == "CHATEAU CHATEAU")):
    #         print("continue 2 ")
    #         continue
    #     # Insérer les lignes de domaines
    #     # Domaine
    #     domaine_id = recupIdApresInsertion(tab_domaine_inverse, domaine, nom.domaine_str, "nom", 1)

liste_appellation_a_enlever = ["CHATEAU D ISSAN", "MOULIS EN MEDOC", "CASTILLON-COTES DE BORDEAUX", "BORDEAUX ROUGE", "LALANDE DE POMEROL", "BLAYE-COTES DE BORDEAUX", "COTES DE BOURG"]

def fct_appellation_id(appellation : str):

    try:

        print("appellation : " + appellation)

        if( appellation in liste_appellation_a_enlever ):
            appellation = "MARGAUX"

        print("appellation : " + appellation)

        appellation_id = req.recuperation_un_id(nom.appellation_str, "appellation", appellation)

        print("appellation_id : " + str(appellation_id))

        if( appellation_id == -1 ):
            erreur_appellation.append("Appellation en erreur : " + appellation)
            appellation_id = 1

        return appellation_id

    except ValueError:
        erreur_appellation.append(appellation + "")

    return 1
    

def insertionVins():

    req.reinitialisation_global([nom.vin_str])

    tuple_valeurs : tuple = ("NA", "NA", 1, 1, 1)
    requete = f"""INSERT INTO """ + nom.vin_str + """(nom, regex, domaine_id, appellation_id, couleur_id) VALUES (%s, %s, %s, %s, %s);"""
    req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs) 

    wb_bis = openpyxl.load_workbook(dest_filename_bis)

    print("dest_filename_bis : " + dest_filename_bis)

    # Lecture du workbook d'origine
    sheet_list = wb_bis.sheetnames  # on récupère le nom des onglets, pas necessaire ici.
    sheet = wb_bis[sheet_list[0]]

    iVinAppellation = sheet['A']
    iCouleur = sheet['B']
    iDomaine = sheet['C']
    iRegion = sheet['D']
    iPays = sheet['E']

    row_count = sheet.max_row

    for i  in range (0, len(liste_vins_rajoutes)):
            
        vin : str = liste_vins_rajoutes[i][0]

        print("vin : " + vin)

        retour_vin : str = ft.retour_premier_element_avec_valeur( liste_vin_a_tester, vin)

        print("retour_vin : " + retour_vin)

        if( retour_vin != "NA"):
            vin = retour_vin

        print("vin : ")
        print(vin)

        domaine = liste_vins_rajoutes[i][2]

        print("domaine : " + domaine)

        domaine_id : int = req.recuperation_un_id(nom.domaine_str, "nom", domaine)

        print("domaine_id : " + str(domaine_id))

        if( domaine_id == -1 ):
            domaine = ft.retour_premier_element_avec_valeur( liste_domaine_a_tester, domaine)

            print("domaine : " + domaine)

            domaine_id : int = req.recuperation_un_id(nom.domaine_str, "nom", domaine)

        print("domaine_id : " + str(domaine_id))

        # Appellation
        appellation : str = liste_vins_rajoutes[i][3]

        appellation_id = fct_appellation_id(appellation)

        print("appellation_id : " + str(appellation_id))

        couleur : str = liste_vins_rajoutes[i][4]

        print("couleur : " + couleur)

        couleur_id : int = req.recuperation_un_id(nom.couleur_vin_str, "couleur", couleur)
        # couleur_id = 1

        print("couleur_id : " + str(couleur_id))

        if(couleur_id == -1):
            couleur = ft.retour_premier_element_avec_valeur(liste_couleur, couleur)

            couleur_id : int = req.recuperation_un_id(nom.couleur_vin_str, "couleur", couleur)

            if( couleur == "NA" ):
                couleur_id = 1

        tuple_valeurs : tuple = (vin, "regex", domaine_id, appellation_id, couleur_id)

        requete = f"""INSERT INTO """ + nom.vin_str + """(nom, regex, domaine_id, appellation_id, couleur_id) VALUES (%s, %s, %s, %s, %s);"""

        req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs) 

    # raise Exception("a", "b")

    for i  in range (1, row_count):
        
        vinApellation = (iVinAppellation[i].value).split(",")

        vin = vinApellation[0]

        appellation : str = "BORDEAUX"

        if( len(vinApellation) == 2 ):
            appellation = vinApellation[1].strip()

        region : str = iRegion[i].value
        couleur : str = iCouleur[i].value
        domaine : str = (iDomaine[i].value).replace("'", " ")
        pays_id : int = iPays[i].value

        # Insérer les lignes de domaines

        # Domaine
        # domaine_id : int = req.recuperation_indice_doublon(nom.domaine_str, "nom", domaine)

        print("domaine  : -" + domaine + "-")

        # Erreur au niveau du domaine
        # domaine_id : int = req.recuperation_un_element(nom.domaine_str, "nom", domaine)
        # domaine_id : int = 2

        domaine_id : int = req.recuperation_un_id(nom.domaine_str, "nom", domaine)

        print("domaine_id : " + str(domaine_id))

        if( domaine_id == -1 ):
            domaine = ft.retour_premier_element_avec_valeur( liste_domaine_a_tester, domaine)

            print("domaine : " + domaine)

            domaine_id : int = req.recuperation_un_id(nom.domaine_str, "nom", domaine)

        print("domaine_id : -" + str(domaine_id) + "-")

        # tab_valeurs_tot = (vin)
        # requete = f"""INSERT INTO domaine(nom) VALUES (%s);"""
        # req.envoie_requete_tuple_sans_retour(requete, tab_valeurs_tot) 

        # Appellation
        appellation_id = fct_appellation_id(appellation)

        print("appellation_id : " + str(appellation_id))

        # tab_valeurs_tot = (vin, "regex", domaine_id, appellation_id, couleur_id)
        # requete = f"""INSERT INTO vin(nom, regex, domaine_id, appellation_id, couleur_id) VALUES (%s, %s, %s, %s, %s);"""
        # req.envoie_requete_tuple_sans_retour(requete, tab_valeurs_tot) 

        # Couleur
        couleur_id : int = ft.retour_premier_element_avec_valeur(liste_couleur, couleur)
        # couleur_id = 1

        # couleur_id : int = req.recuperation_indice_doublon(nom.couleur_vin_str, "couleur", couleur)

        print("couleur : " + couleur)

        couleur_id : int = req.recuperation_un_id(nom.couleur_vin_str, "couleur", couleur)
        # couleur_id = 1

        print("couleur_id : " + str(couleur_id))

        if(couleur_id == -1):
            couleur = ft.retour_premier_element_avec_valeur(liste_couleur, couleur)

            print("couleur : -" + couleur + "-")

            couleur_id : int = req.recuperation_un_id(nom.couleur_vin_str, "couleur", couleur)

            if( couleur == "NA" ):
                couleur_id = 1

        # couleur_id : int = recupId(tab_couleur_vin, couleur, nom.couleur_vin_str, "couleur", 1)

        # print("vin : " + vin + " regex : " + str(domaine_id) + " appellation_id : " + str(appellation_id) + " couleur_id : " + str(couleur_id))

        print("vin : -" + str(vin) + "-")

        tuple_valeurs : tuple = (vin, "regex", domaine_id, appellation_id, couleur_id)
        requete = f"""INSERT INTO """ + nom.vin_str + """(nom, regex, domaine_id, appellation_id, couleur_id) VALUES (%s, %s, %s, %s, %s);"""
        req.envoie_requete_tuple_sans_retour(requete, tuple_valeurs) 
        
def recuperationVins():

    try:

        print("Démarrage du formattage du fichier pour les domaines et les vins : " + str(datetime.now()))

        formaterFichierLWIN()

        print("Fin du formattage du fichier pour les domaines et les vins : " + str(datetime.now()))

        print("Insertion des domaines : " + str(datetime.now()))

        insertionDomaines()

        # L'insertion des vins passe avant l'insertion des domaines, comme le vin a une clef secondaire de domaine affiche une erreur.
        time.sleep(2)

        # tab_domaine = req.recuperation_tab( nom.domaine_str )
        # tab_domaine_inverse = list(map(list, np.transpose(tab_domaine)))

        print("Fin insertion des domaines : " + str(datetime.now()))

        print("Insertion des vins : " + str(datetime.now()))
        
        insertionVins()

        print("Fin insertion des vins : " + str(datetime.now()))

        # Les erreurs
        print("Les erreurs : ")
        print(erreur_appellation)

    except Exception as erreur :
        print(type(erreur))    # the exception instance
        print(erreur.args)     # arguments stored in .args
        print(erreur)

    os.remove(dest_filename_bis)
    os.remove(dest_filename)

recuperationVins()










   

