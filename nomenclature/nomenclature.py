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



