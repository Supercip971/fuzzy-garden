
class GraphLink: 
    lhs: str 
    rhs: str
    weight: int

    def __init__(self, lhs, rhs, weight):
        self.lhs = str(lhs)
        self.rhs = str(rhs)
        self.weight = weight

    def __str__(self):
        return f"({self.lhs} <-> {self.rhs}, {self.weight})"
    
graph = [
    GraphLink(6,4,30),
    GraphLink(6,0,20),
    GraphLink(5,0,50),
    GraphLink(5,4,40),
    GraphLink(4,0,20),
    GraphLink(4,1,50),
    GraphLink(4,3,40),
    GraphLink(4,2,50),
    GraphLink(3,2,20),
    GraphLink(3,0,50),
    GraphLink(2,0,40),
    GraphLink(2,1,30),
    GraphLink(1,0,30),
]

def get_nodes(graph: list[GraphLink]) -> list[str]:
    nodes = []
    for link in graph: 
        if link.lhs  not in nodes:
            nodes.append(link.lhs)
        if link.rhs  not in nodes:
            nodes.append(link.rhs)
    return nodes 



# graph is in the form: 
# { key: {path }

# starts = R
# end = E

def choose_min_path(graph: list[GraphLink], starts: list[str]) -> str:
    min_path = None
    min_weight = None

    for link in graph:
        if min_weight is None or link.weight < min_weight:
            if link.lhs in starts and not link.rhs in starts:
                min_weight = link.weight
                min_path = link
            elif link.rhs in starts and not link.lhs in starts:
                min_weight = link.weight
                min_path = link

    return min_path

def min_couv(graph: list[GraphLink], initial_point: str):
    r: list[str] = [initial_point]
    e: list[GraphLink] = graph.copy()
    cmg: list[GraphLink] = []
    
    lnub = len(get_nodes(graph))
    while len(r) < lnub:
        min_path = choose_min_path(e, r)
        if(min_path is None):
            break
        cmg.append(min_path)
        
        if min_path.lhs not in r:
            r.append(min_path.lhs)
        if min_path.rhs not in r:
            r.append(min_path.rhs)
        
        print(min_path)
        e.remove(min_path)
    
    return cmg 

print(min_couv(graph, "0"))
