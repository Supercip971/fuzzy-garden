
import csv

bio_indicateurs_data = []

def bio_indicateur_espece(espece):
    """
    Retourne la liste des bio-indicateurs de l'espèce passée en paramètre.
    
    Paramètres
    ----------
    espece : str
        Nom de l'espèce dont on veut les bio-indicateurs.
    
    Retourne
    -------
    bio_indicateurs : list
        Liste des bio-indicateurs de l'espèce passée en paramètre.
    """

    for i in bio_indicateurs_data:
        if i[0] == espece:
            return i[1:]
    return None

def bio_indicateurs_init(): 
    """
    Charge les bio-indicateurs depuis le fichier 'data_sommets_bioindicateurs.csv' dans la 
    variable globale bio_indicateurs_data.
    """
    data = []    

    with open("data/data_sommets_bioindicateurs.csv", encoding="utf-8") as f_bioind:
        r_bioind = csv.reader(f_bioind, delimiter=";")
        data = [row for row in r_bioind]  # vu que r_bioind est un reader, on lit toutes les entrées dans un tableau (r_bioind n'est pas un tableau <!>)

    return data

# Plus le score est bas 
def bio_indicateurs_malus(el1, el2):
    esp1 = bio_indicateur_espece(el1)
    esp2 = bio_indicateur_espece(el2)
    
    # si l'une des deux espèces n'est pas listée, nous ne considérons pas de malus 
    if esp1 == None or esp2 == None: 
        return 0

    # si les deux espèces sont listées, nous calculons le malus par la distance 
    # entre les deux espèces
    # pour chaque bio indicateur, on calcule la distance 
    #   dist = somme |esp1_i - esp2_i|

    dist = 0
    for i in range(len(esp1)):
        dist += abs(float(esp1[i]) - float(esp2[i]))
    
    return dist
    
    
bio_indicateurs_data = bio_indicateurs_init()