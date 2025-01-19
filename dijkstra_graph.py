import math

def d_init(o_graph, s_deb):
    """ 
    initialise les distances entre s_deb et les autres noeuds de o_graph, à 0 pour s_deb, à l'infini pour les autres
    
    Paramètres
    ----------
    o_graph : dict
        graphe orienté
    s_deb : str
        noeud de départ
    Retourne
    -------
    dist : dict
        dictionnaire initialisé des distances entre un noeud de o_graph et s_deb."""
    dist = {}
    
    #affectation d'une distance infinie pour tous les noeuds de o_graph
    
    for som in o_graph.keys():
        dist[som] = math.inf
    
    #affectation d'une distance de 0 pour s_deb
    
    dist[s_deb] = 0
    return dist


def find_min(n_list, dico_dist):
    """
   Trouve le sommet de plus faible distance au noeud de départ
    
    Paramètres
    ----------
    n_list : list
        liste de noeuds
    dico_dist : dict
        dictionnaire contenant les distances entre un noeud et le noeud de départ
    
    Retourne
    -------
    s_min : str
        sommet de plus courte distance"""
    mini = math.inf
    
    #on parcourt les noeuds dans la liste de noeuds.
    #si la distance du noeud regardé est plus petite que la valeur minimale
    #alors le noeud regardé devient le noeud de distance minimale
    
    for s in n_list: 
        if  dico_dist[s] <= mini: 
            mini = dico_dist[s]
            s_min = s
        
    return s_min
  
    
def maj_dist(dist, n1, n2, pred, graph):
    """
    Met à jour la distance entre deux noeuds.
    
    Paramètres
    ----------
    dist : dict
        dictionnaires des distances entre les noeuds
    n1 : str
        noeud
    n2 : str
        noeud
    pred : dict
        dictionnaires des prédécesseurs d'un noeud
    graph : dict
        
    Retourne
    -------
    dist : dict
    pred : dict"""
    
    p = poids(n1, n2, graph)
    
    if dist[n2] > dist[n1] + p: #on vérifie s'il est mieux de passer par n1 ou non
        dist[n2] = dist[n1] + p
        pred[n2] = n1 # on créée un chemin de n1 vers n2, donc n1 devient le prédecesseur de n2
        
    return dist, pred  


def poids(n1, n2, graph):
    
    for arc in graph[n1]:
        if arc[1] == n2 : 
            return arc[0]
    
    print(f"j'ai pas trouvé: {n1} {n2}")

def find_shortest_path(s_deb, s_fin, pred):
    short_path = [] 
    som = s_fin  
    ptot = 0

    while som != s_deb : 
        short_path = [som] + short_path
        
        # Si dans un chemin nous n'avons pas trouvé un prédécesseur
        if not som in pred.keys(): 
            print(f"Erreur: aucun chemin possible n'a été trouvé entre: {s_deb} et {s_fin}")
            return []

        som = pred[som]
        
    short_path = [s_deb] + short_path

    return short_path


def dijkstra(o_graph, s_deb, s_fin):
    dico_dist = d_init(o_graph, s_deb) #init de la distance
    to_visit = [s for s in o_graph.keys()]
    pred = {}    
    
    while to_visit != []:     #tant que tous les sommets de o_graph ne sont pas dans d_graph
        s = find_min(to_visit, dico_dist)
        to_visit.remove(s)
        
        arc_vois = o_graph[s]
        voisin = [arc_vois[i][1] for i in range(len(arc_vois)) ]
        # o_graph est de la forme : {a:[[1,b], [2,c]]}
        
        for v in voisin : 
            dico_dist, pred = maj_dist(dico_dist, s, v, pred, o_graph)

    return find_shortest_path(s_deb, s_fin, pred), dico_dist[s_fin]