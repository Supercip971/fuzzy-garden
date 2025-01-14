import csv
import ds_graph as g
import arcs as arc 

A=str(input("premier indrédient : ")) 
B=str(input('2e ingrédient : '))  

print(g.chemin(arc.list_to_dico(arc.arcs), A, B))

