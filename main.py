import csv
import ds_graph as g

def list_to_dico(liste):
    """Entrée : liste (list)
    ---
    convertit une liste de listes de taille 3 en dico
    ---
    Sortie : dico (dict)"""
    
    dico = {}
    for elt in liste:
        if elt[1] == 'favorise':
            dico[elt[0]] = dico.get(elt[0],[]) + [elt[2]]

    return(dico)

#récupérer les data du fichier data arcs
with open("data/data_arcs.csv") as f_arcs:
    r_arcs = csv.reader(f_arcs, delimiter=";")
    arcs = [row for row in r_arcs]  #liste de liste avec les arcs
 
 
A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  
print(g.chemin(list_to_dico(arcs), A, B))
    