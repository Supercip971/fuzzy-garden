

import arcs as arc

def print_chemin_defavorisee_element(path, defavorise, element):
    """
    On rappelle que la structure retournée par 
    arc.list_to_dico() 
    est de la forme: 
    adj = {
        # Exemple: A -> B (poids 10)
        # A -> C (poids 20)
        'a' : [ [10,'b'], [20,'c'] ], #choix de l'ordre alphabétique pour les sommets adjacents d'un sommet
        'b' : [ [30,'a'], [0,'e'], [-1,'h'] ],
    }
    """

    if not element in defavorise.keys():
        return 

    """
    Pour chaque élément unique du chemin (un élément peut apparaitre plusieurs fois)
    Pour chaque élément défavorisé avec l'élément en question,
    On affiche un arc rouge entre les deux éléments.
    """
    for echemin in set(path):   
        for sub_elt in defavorise[element]:
           # on rappelle que le premier éléments représente le poids
            # le second le nom du noeud.
            nom = sub_elt[1]

            if echemin == nom:
                print(f'    "{element}" -> "{nom}" [color=Red, label="defavorise"]')


def print_chemin(path):
    arcs = arc.arcs
    """
    Depuis un chemin 'path', et les données arcs importées depuis data_arcs_poids.csv
    on génère un script .dot qui permet de visualiser le chemin favorisé.
    Il affiche également les éléments qui sont défavorisés entre eux.
    """ 
    
    defavorise = arc.list_to_dico(arcs, type_lien='defavorise')
    
    
    print("========= RESULTAT DOT ========")
    print("digraph {")
    print("    layout=circo")
    
    for i in range(len(path)-1):
        print(f'    "{path[i]}" -> "{path[i+1]}" [color=Blue, label="favorise"]')     
    
    # la fonction set permet de ne pas avoir de doublons
    # on aura forcément un doublon vu que l'on fait un cycle.
    for node in set(path):
        print_chemin_defavorisee_element(path, defavorise, node)
     
    print("}")

