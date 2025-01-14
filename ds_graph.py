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

