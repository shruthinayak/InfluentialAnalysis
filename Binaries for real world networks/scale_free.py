import matplotlib.pyplot as plt
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
import itertools
import random
import math
import degreeDistribution as d
#from collections import defaultdict

def _random_subset(seq,m):
    
    print "Entered"
    targets=set()
    while len(targets)<m:
        x=random.choice(seq)
        targets.add(x)
    #print targets
    return targets

def scalefree_graph(n, m):
   
       
	# Add m initial nodes (m0 in barabasi-speak) 
	G=empty_graph(m)
	#G.name="barabasi_albert_graph(%s,%s)"%(n,m)
	# Target nodes for new edges
	#nx.draw(G)
	#plt.show()
	targets=list(range(m))
	sample=[]
	print "Targets:",targets
	# List of existing nodes, with nodes repeated once for each adjacent edge 
	repeated_nodes=[]     
	# Start adding the other n-m nodes. The first node is m.
	source=m 
	while source<n: 
		# Add edges to m nodes from the source.
		#print zip([source]*m,targets)
		G.add_edges_from(zip([source]*m,targets)) 
		# Add one node to the list for each new edge just created.
		repeated_nodes.extend(targets)
		sample.append(targets)
		# And the new node "source" has m edges to add to the list.
		repeated_nodes.extend([source]*m) 
		sample.append([source]*m)
		# Now choose m unique nodes from the existing nodes 
		# Pick uniformly from repeated_nodes (preferential attachement) 
		targets = _random_subset(repeated_nodes,m)
		source += 1
	#print "T",targets
	#print "S " ,sample
	return G
G=scalefree_graph(10,2)
#d.plotdegree2("Scale-Free","Degree","Count",G)
nx.draw(G)
plt.show()
