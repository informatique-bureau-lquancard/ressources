import glob
import openpyxl
from unidecode import unidecode

def recuperation_appellations():
    
    wb = openpyxl.load_workbook("/var/www/html/ressources/nomenclature/appellations/Vins_listes.xlsx")

    # Lecture du workbook d'origine
    sheet_list = wb.sheetnames  # on récupère le nom des onglets, pas necessaire ici.
    sheet = wb[sheet_list[0]]

    iAppellation = sheet['A']

    row_count = sheet.max_row

    print("row_count : " + str(row_count))

    liste_appellation : list = []

    liste_appellation.append("NA")

    for i  in range (1, row_count):
                
        appellation : str = unidecode(str(iAppellation[i].value)).upper().strip()

        appellation = appellation.replace("'", "")

        if( (appellation is None) or (appellation == "APPELLATIONS")):
            continue;
        
        liste_appellation.append(appellation)

    return liste_appellation

        