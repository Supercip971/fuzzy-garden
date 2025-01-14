import csv
import ds_graph as g


def list_to_dico(liste):
    """
    Convertit une liste de listes de taille 3 en dico
    
    Paramètres
    ----------
    liste : list
        Liste à convertire au format de liste de liste, importée du fichier data_arcs.csv
    
    Retourne
    -------
    dico : dict
        Dictionnaire qui associe chaque entrée au destinations favorisées possibles
    """
    
    dico = {}
    for elt in liste:
        if elt[1] == 'favorise':
            # FIXME: A réécrire c'est degueu ça 
            # on dois réfléchir pour comprendre ce que ça fait
            # <?> un bon code ne dois pas bloquer à la compréhension d'un algo  
            dico[elt[0]] = dico.get(elt[0],[]) + [elt[2]]

    return(dico)


list_to_dico()

# Récupérer les data du fichier data arcs
with open("data/data_arcs.csv", encoding="utf-8") as f_arcs:
    r_arcs = csv.reader(f_arcs, delimiter=";")
    arcs = [row for row in r_arcs]  #liste de liste avec les arcs

 
A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  
print(g.chemin(list_to_dico(arcs), A, B))
