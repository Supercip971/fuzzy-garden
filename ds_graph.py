def bfs(adj, s_init):
    """ 
    applique le bfs sur un graphe
    Paramètres
    ----------
    adj : list
        liste des noeuds adjacents au noeud de départ
    s_init : str
        noeud de départ
    Retourne
    -------
    dist : dict
        dictionnaire initialisé des distances entre un noeud de o_graph et s_deb."""
    q = [s_init]    #noeuds à vister
    parent = {}
    visited = [s_init]  #noeuds déjà visités

    while len(q) > 0:
        u = q.pop(0)
        if u in adj: 
            for v in adj[u]:
                if not v in visited:    #on vérifie que le noeud n'a pas déjà été visté
                    visited.append(v)
                    parent[v] = u 
                    q.append(v) # on ajoute v à la liste des noeuds visités

    return parent 


def chemin(adj, root, v):
    """ 
    trouve le plus court chemin entre deux noeuds
    
    Paramètres
    ----------
    adj : list
        liste des noeuds adjacents au noeud de départ
    root : str
        noeud de départ
    v : str
        dictionnaire des prédécesseurs d'un noeud

    Retourne
    -------
    chemin : list
        liste contenant le plus court chemin entre deux noeuds"""
    l = bfs(adj, root)

    if root == v: 
        return [root] 
    elif not v in l.keys(): 
        return []  
    else: 
        p = chemin(adj, root, l[v])
        return p + [v]

