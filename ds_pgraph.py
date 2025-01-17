import math

def d_init(o_graph, s):
    """ initialiser les distances"""
    dist = {}
    
    for som in o_graph.keys():
        dist[som] = math.inf
    
    dist[s] = 0
    return dist


def find_min(n_list, dico_dist):
    mini = math.inf
     
    for s in n_list : 
        
        if  dico_dist[s] < mini : 
            mini = dico_dist[s]
            s_min = s
        
    return s_min
  
    
def maj_dist(dist, n1, n2, pred):
    p = poids(n1, n2)
    
    if dist[n1] > dist[n2] + p:
        dist[n2] = dist[n1] + p
        pred[n2] = n1
        
    return dist, pred


def poids(n1, n2, graph):
    
    for arc in graph[n1].values():
        if arc[1] == n2 : 
            return arc[0]
    print("j'ai pas trouvé") 
    
    
def Dijkstra(o_graph, s_deb, s_fin):
    d_graph = {}
    dico_dist = d_init(o_graph, s_deb) #init de la distance
    to_visit = [s for s in o_graph.keys()]
    short_path = [] 
    som = s_fin  
    
    while to_visit != []:     #tant que tous les sommets de o_graph ne sont pas dans d_graph
        s = find_min(to_visit, dico_dist)
        to_visit.remove(s)
        vois = [o_graph[s][i][1] for i in range(len(o_graph[s])) ]
        pred = {}
        # o_graph est de la forme : {a:[[1,b], [2,c]]}
        
        for v in vois : 
            dico_dist, pred = maj_dist(dico_dist, s, v, pred)
    
    while som != s_deb : 
        short_path = [som] + short_path
        som = pred[som]
        
    short_path = [s_deb] + short_path
    return short_path

   
