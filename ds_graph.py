###############
### Fonctions

def valeur_exploree(stack, x):
    for v in stack:
        for i in v:
            if i == x:
                return True 

    return False

def affiche_largeur(s_init, adj) :
    '''
    s_init : sommet initial
    adj : dico associant la liste des suivants à tout sommet ayant au moins un suivant
    type des sommets quelconques pourvu qu'il y ait cohérence entre éléments de la liste et du dico.
    ne retourne rien, fait juste un affichage
    '''
    levels = [] 
    levels.append([s_init])

    a_explorer = [s_init] 
    while len(a_explorer) > 0:
        niveau = []
        for v in a_explorer:
            
            if not v in adj.keys():
                continue
        
            enfants = adj[v]
            for e in enfants: 
                if not valeur_exploree(levels, e) and not e in niveau:
                    niveau.append(e)
        
        if len(niveau) != 0:
            levels.append(niveau)
        
        a_explorer.clear()
        for v in niveau:
            a_explorer.append(v)
    print(levels)
    return levels
    


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



## affichage des noeuds dans l'ordre du parcours en largeur à partir de a
#print("Parcours en largeur à partir de 'a'")
#affiche_largeur('a', adj)

#print()

## affichage des noeuds dans l'ordre du parcours en largeur à partir de c
#print("Parcours en largeur à partir de 'c'")
#affiche_largeur('c', adj)


print(chemin(adj, 'c', 'f'))
