### Ce fichier sert juste à lancer le fichier "nomenclature.py" ###

import initialisation_bd_blq as init_bd_blq

# import sys
# sys.path.append("/var/www/html/ressources/nomenclature/domainesVins")
# import traitement_domaines_vins as tdv

# Permet 2 accès au fichier "nomenclature.py" :
# 1 Récupération des données (avec les imports)
# 2 Réinitilisation des tables (avec le fichier "nomenclature_test.py")

def main():
    
    # Lancement du fichier "nomenclature.py"
    init_bd_blq.main() 

    # Ne marche pas
    # Lancement du fichier "traitement_domaines_vins.py"
    # tdv.recuperationVins()

main()