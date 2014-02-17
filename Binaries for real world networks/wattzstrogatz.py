import matplotlib.pyplot as plt
import itertools
import random
import math
import networkx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
#import degreeDistribution as d
def watts_strogatz_graph(n, k, p, create_using=None, seed=None):
    """Return a Watts-Strogatz small-world graph.
    """
    if create_using is None:
        G = networkx.Graph()
    elif create_using.is_directed():
        raise networkx.NetworkXError("Directed Graph not supported")
    else:
        G = create_using
        G.clear()

    if seed is not None:
        random.seed(seed)

    G.name="watts_strogatz_graph(%s,%s,%s)"%(n,k,p)
    nodes = range(n) # nodes are labeled 0 to n-1
    # connect each node to k/2 neighbors
    for j in range(1, k/2+1):
        targets = nodes[j:] + nodes[0:j] # first j nodes are now last in list
        G.add_edges_from(zip(nodes,targets))
    # rewire edges from each node
    # loop over all nodes in order (label) and neighbors in order (distance)
    # no self loops or multiple edges allowed
    for j in range(1, k/2+1): # outer loop is neighbors
        targets = nodes[j:] + nodes[0:j] # first j nodes are now last in list
        # inner loop in node order
        for u,v in zip(nodes,targets): 
            if random.random() < p:
                w = random.choice(nodes)
                # Enforce no self-loops or multiple edges
                while w == u or G.has_edge(u, w): 
                    w = random.choice(nodes)
                G.remove_edge(u,v)  
                G.add_edge(u,w)
    return G 
G=watts_strogatz_graph(234, 9, 0.2) 
networkx.draw(G)
plt.savefig("graph.png") 
#d.plotdegree2("WattzStrogatz", "Degree","Count",G)
#plt.show()
