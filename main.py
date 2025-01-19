import csv
import ds_graph as g
import arcs as arc 
import dijkstra_graph as dg
import render as rdot

A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  

graph = arc.list_to_dico(arc.arcs)
chem,poids = dg.dijkstra_cycle(graph, A, B)

biograph = arc.list_to_dico(arc.arcs, utilise_bioind=True)
biochem, biopoids = dg.dijkstra_cycle(biograph, A, B)

print(" === Sans bioindicateurs === ")
print(f'chemin: {chem}')
print(f'poids: {poids}')

print(" === Avec bioindicateurs === ")
print(f'chemin: {biochem}')
print(f'poids: {biopoids}')

print(" === Visualisation (dot) ===")
rdot.print_chemin(chem)