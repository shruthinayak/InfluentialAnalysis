import networkx as nx
import matplotlib.pyplot as plt
import math
import commonfunctions as cf
G = cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
""" Generate THE GRAPH"""
#FOR ERDOS RENYI
#G=nx.erdos_renyi_graph(8114,0.00079) 421578
#G=nx.watts_strogatz_graph(235,8,0.2)
#G=nx.erdos_renyi_graph(235,0.076)
#G=nx.barabasi_albert_graph(235,8)
nodes=G.order()
edges=len(G.edges())
print "edges",edges
print "nodes",nodes
avg_degree=float(nodes)/edges
deg={}
summ=0
for i in G.nodes():
	summ=summ+G.degree(i)
print summ
avg_path_l=summ/nodes
avg_path_len=float(math.log(nodes))/(math.log(avg_path_l))
print avg_path_len

#erdos=7.75
#watts=12.98
#cluster=float(1)/nodes
#print cluster
