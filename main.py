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
            dico[elt[0]] = dico.get(elt[0], [])
            dico[elt[0]].append([elt[3], elt[2]]) # donne poids -> destination

    return(dico)


# exemple de liste retournée par list_to_dico:
adj = {
    # Exemple: A -> B (poids 10)
    # A -> C (poids 20)
    'a' : [ [10,'b'], [20,'c'] ], #choix de l'ordre alphabétique pour les sommets adjacents d'un sommet
    'b' : [ [30,'a'], [0,'e'], [-1,'h'] ],
    'c' : [ [30,'d'], [2,'e'] ],
    'd' : [ [0,'e'] ],
    'e' : [ [4,'f'], [3,'g']],
    'f' : [ [1,'g'] ],
    'h' : [[999,'i']],
}



list_to_dico()

# Récupérer les data du fichier data arcs
with open("data/data_arcs_poids.csv", encoding="utf-8") as f_arcs:
    r_arcs = csv.reader(f_arcs, delimiter=";")
    arcs = [row for row in r_arcs]  #liste de liste avec les arcs

 
A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  
print(g.chemin(list_to_dico(arcs), A, B))
