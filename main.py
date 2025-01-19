import csv
import ds_graph as g
import arcs as arc 
import dijkstra_graph as dg

A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  

tree = arc.list_to_dico(arc.arcs)
chem = dg.dijkstra(tree, A, B)

print(f'chemin: {chem}')
print(f'poids: {dg.poids_total(tree, chem)}')


