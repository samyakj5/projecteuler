import numpy as np
import networkx as nx

with open("problem0107_data.txt", "r", encoding="utf-8") as file:
    edges = file.read().split("\n")

G = nx.Graph()

for i in range(len(edges)):
    e = edges[i].split(",")
    for j in range(len(e)):
        if e[j] == "-":
            continue
        G.add_edge(i, j, weight=int(e[j]))

mst = nx.minimum_spanning_tree(G)

print(int(G.size(weight='weight') - mst.size(weight='weight')))