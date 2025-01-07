def bfs(adj, s_init):
    q = [s_init]
    parent = {}
    visited = [s_init]

    while len(q) > 0:
        u = q.pop(0)
        if u in adj: 
            for v in adj[u]:
                if not v in visited:
                    visited.append(v)
                    parent[v] = u 
                    q.append(v) 

    return parent 

def chemin(adj, root, v):
    l = bfs(adj, root)

    if root == v: 
        return [root] 
    elif not v in l.keys(): 
        return []  
    else: 
        p = chemin(adj, root, l[v])
        return p + [v]




 
###############
### Code principal

## Définition d'un graphe
## Représentation choisie : 
## - une liste de sommets et 
## - un dictionnaire associant à chaque sommet la liste des sommets adjacents (quand il y a des sommets)


sommets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

adj = {
'a' : [ 'b', 'c' ], #choix de l'ordre alphabétique pour les sommets adjacents d'un sommet
'b' : [ 'a', 'e', 'h' ],
'c' : [ 'd', 'e' ],
'd':  [ 'e' ],
'e' : [ 'f', 'g'],
'f' :  [ 'g' ],
'h' : ['i'],
}


