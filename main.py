import csv
import ds_graph as g

#récupérer les data du fichier data arcs
with open("data/data_arcs.csv") as f_arcs:
    r_arcs = csv.reader(f_arcs)
    arcs = [row for row in r_arcs]  #liste de liste avec les arcs
    
def list_to_dico(liste):
    dico = {}
    for elt in liste:
        if elt[1] == 'favorise':
            dico[elt[0]] = dico.get(elt[0],[]) + [elt[2]]

    