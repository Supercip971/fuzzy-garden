def bfs(o_graph, s_deb):
    """ 
    applique le bfs sur un graphe
    Paramètres
    ----------
    o_graph : list
        liste des noeuds adjacents au noeud de départ
    s_deb : str
        noeud de départ
    Retourne
    -------
    dist : dict
        dictionnaire initialisé des distances entre un noeud de o_graph et s_deb.
    """
    
    q = [s_deb]         # noeuds à vister
    pred = {}           # predecesseur
    visitee = [s_deb]   # noeuds déjà visités

    while len(q) > 0:
        a_visiter = q.pop(0)
        if a_visiter in o_graph.keys(): 
            for v in o_graph[a_visiter]:
                # o_graph est de la forme : {a:[[1,b], [2,c]]}
                nom_noeud = v[1]
                if not nom_noeud in visitee:    # on vérifie que le noeud n'a pas déjà été visté
                    visitee.append(nom_noeud)   # on ajoute le noeud aux noeud déjà visités
                    pred[nom_noeud] = a_visiter 
                    q.append(nom_noeud)

    return pred 


def chemin(o_graph, s_deb, s_fin):
    """ 
    Trouve le plus court chemin entre deux noeuds
    
    Paramètres
    ----------
    o_graph : list
        liste des noeuds adjacents au noeud de départ
    s_deb : str
        noeud de départ
    s_fin : str
        noeud de fin

    Retourne
    -------
    chemin : list
        liste contenant le plus court chemin entre deux noeuds
    """
    
    l = bfs(o_graph, s_deb)

    if s_deb == s_fin: 
        return [s_deb] 
    elif not s_fin in l.keys(): 
        return []  
    else: 
        p = chemin(o_graph, s_deb, l[s_fin])
        return p + [s_fin]

