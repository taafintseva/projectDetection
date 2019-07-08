import networkx as nx
import matplotlib.pyplot as plt
import vk
import numpy as np
import random
import requests
import json
import math
G = nx.Graph()
e = [('a','b'),('b','c'),('a','c'),('c','d')]
G.add_edges_from(e)
def gcut(G):
    number = G.number_of_nodes()
    while number >= 2:
        e = random.choice(list(G.edges()))
        G.remove_edge(*e)
        number = number-1
        print(number)
    return G.number_of_edges()
gcut(G)
nx.draw(G, with_labels=True,node_color = 'pink')
plt.savefig("edge_colormap.png")
plt.show()
