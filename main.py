import csv
import ds_graph as g
import arcs as arc 
import dijkstra_graph as dg

A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  

graph = arc.list_to_dico(arc.arcs)
chem = dg.dijkstra(graph, A, B)

biograph = arc.list_to_dico(arc.arcs, utilise_bioind=True)
biochem = dg.dijkstra(biograph, A, B)


print(" === Sans bioindicateurs === ")
print(f'chemin: {chem}')
print(f'poids: {dg.poids_total(graph, chem)}')

print(" === Avec bioindicateurs === ")
print(f'chemin: {biochem}')
print(f'poids: {dg.poids_total(biograph, biochem)}')



