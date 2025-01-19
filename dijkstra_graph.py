import math

def d_init(o_graph, s_deb):
    """ initialiser les distances"""
    dist = {}
    
    for som in o_graph.keys():
        dist[som] = math.inf
    
    dist[s_deb] = 0
    return dist


def find_min(n_list, dico_dist):
    mini = math.inf
    
    for s in n_list: 
        if  dico_dist[s] <= mini: 
            mini = dico_dist[s]
            s_min = s
        
    return s_min
  
    
def maj_dist(dist, n1, n2, pred, graph):
    p = poids(n1, n2, graph)
    
    if dist[n2] > dist[n1] + p:
        dist[n2] = dist[n1] + p
        pred[n2] = n1
        
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

def poids_total(o_graph, chemin):
    ptot = 0
    
    for v in range(len(chemin)-1):
        ptot += poids(chemin[v], chemin[v+1], o_graph)
        
    return ptot
        

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

    return find_shortest_path(s_deb, s_fin, pred)