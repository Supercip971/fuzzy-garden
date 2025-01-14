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
    

def Dijkstra(o_graph, s_deb):
    d_graph = {}
    dico_dist = d_init(o_graph, s_deb) #init de la distance
    to_visit = [s for s in o_graph.keys()]
    
    while to_visit != []:     #tant que tous les sommets de o_graph ne sont pas dans d_graph
        s = find_min(to_visit, dico_dist)
        to_visit.remove(s)
        
        