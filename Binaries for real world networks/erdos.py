
#!/usr/bin/env python

import sys
import itertools
import random
import math
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.classic import empty_graph, path_graph, complete_graph
#import degreeDistribution as d

"""
def gnm_random_graph(n, m, seed=None, directed=False):
  
    if directed:
        G=nx.DiGraph()
    else:
        G=nx.Graph()
    G.add_nodes_from(range(n))
    G.name="gnm_random_graph(%s,%s)"%(n,m)

    if seed is not None:
        random.seed(seed)

    if n==1:
        return G
    max_edges=n*(n-1)
    if not directed:
        max_edges/=2.0
    if m>=max_edges:
        return complete_graph(n,create_using=G)

    nlist=G.nodes()
    print nlist
    edge_count=0
    while edge_count < m:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        print u,v
        if u==v or G.has_edge(u,v):
            continue
        else:
            #print "Entered"
            G.add_edge(u,v)
            edge_count=edge_count+1
    return G
"""   
    
def gnp_random_graph(n, p, seed=None, directed=False):
    
    if directed:
        G=nx.DiGraph()
    else:
        G=nx.Graph()
    G.add_nodes_from(range(n))
    G.name="gnp_random_graph(%s,%s)"%(n,p)
    if p<=0:
        return G
    if p>=1:
        return complete_graph(n,create_using=G)

    if not seed is None:
        random.seed(seed)

    if G.is_directed():
        edges=itertools.permutations(range(n),2)
    else:
        edges=itertools.combinations(range(n),2)

    for e in edges:
        if random.random() < p:        
            G.add_edge(*e)
    return G


n=234 # 10 nodes
m=2100 # 20 edges
#m=p*n*(n-1)/2
p=float(m*2)/(n*(n-1))
print p
#G=gnm_random_graph(n,m)
G=gnp_random_graph(n,p)
#d.plotdegree2("Erdos-Reyni","Degree","Count",G)
nx.draw(G)
plt.show()
#print nx.edges(G)

# print the adjacency list to terminal 
try:
    nx.write_adjlist(G,"erdos.adjlist")
except TypeError: 
    nx.write_adjlist(G,sys.stdout.buffer)


