import math

def d_init(o_graph, s):
    """ initialiser les distances"""
    dist = {}
    for som in o_graph.keys():
        dist[som] = math.inf
    
    dist[s] = 0

def isCouvrant(g1, g2): 
    """ regarde si g1 est un graphe couvrant de g2 (tous ses noeuds sont dedans)"""
    for s in g1.keys(): 
        if s not in g2.keys():
            return False
        
    return True

def dijkstra(o_graph, s_deb):
    d_graph = {}
    dist_graph = d_init(o_graph, s_deb)
    