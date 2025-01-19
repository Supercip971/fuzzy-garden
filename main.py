import csv
import ds_graph as g
import arcs as arc 
import dijkstra_graph as dg

A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  

graph = arc.list_to_dico(arc.arcs)
chem,poids = dg.dijkstra(graph, A, B)

biograph = arc.list_to_dico(arc.arcs, utilise_bioind=True)
biochem, biopoids = dg.dijkstra(biograph, A, B)


print(" === Sans bioindicateurs === ")
print(f'chemin: {chem}')
print(f'poids: {poids}')

print(" === Avec bioindicateurs === ")
print(f'chemin: {biochem}')
print(f'poids: {biopoids}')



