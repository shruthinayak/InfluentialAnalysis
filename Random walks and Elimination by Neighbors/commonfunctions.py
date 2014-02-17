import math
from random import choice
import networkx as nx
import pickle
import time
import matplotlib.pyplot as plt
level=2
def top_e_log_n(hotspots,n):
	hubs=[]
	
	m=math.e*math.log(n)
	m= int (m)
	for i in range(0,n):
		hubs.append(hotspots[i])
	return hubs

def sort_dict(d):
	asc=[]
	for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
		asc.append(key)
	asc.reverse()
	return asc

def num_of_same_nodes_in_paths(path1, path2):
	''' Input: Takes 2 lists representing paths,
	Returns: Number of common nodes between the two paths'''
	sim_nodes=[]
	count=0
	for i in path1:
		if(path2.count(i)):
			count =count+1
			sim_nodes.append(i)	
	print "Num of sim nodes: ",count
	return sim_nodes
	
def degreeRank(G,n):
	ts = time.time()
	deg = nx.degree_centrality(G)
	degs=sort_dict(deg)
	asc = top_e_log_n(degs,n)
	cnd = network_coverage(G,asc,level)
	te=time.time()
	print "Time taken for Degree:",round(te-ts,2)
	return cnd

# Verification #

def meet_hotspot(G,hubs):
	count=0
	encounter=0
	nodes = G.nodes()
	for i in nodes:
		if i not in hubs:
			count=count+1
			current=i
			path=[]
			pathlen=0
			while(pathlen!=2):
				neigh = G.neighbors(current)
				path.append(current)
				nextnode = choice(neigh)
				trial =0
				while trial<4 and nextnode in path:
					trial=trial+1
					nextnode = choice(neigh)
				current=nextnode
				pathlen=pathlen+1
			print path
			print hubs
			for node in hubs:
				if node in path:
					encounter=encounter+1
	print "Hotspots encountered:",encounter
	print "Total count:",count
	print "Probablitity:",encounter/(count*1.0)
	
cn=0
ct=0

def network_coverage(G,hubs,level):
	
	coverage=0
	count=0
	graph={}
	total=[]
	n=G.number_of_nodes()
	for i in hubs:
		if (coverage==1.0):
			break
		else:
			total = net_cov(G,i,level,total)
			coverage = round(len(total)/(n*1.0),3)
	
	print len(hubs),"Network coverage = ",(coverage*100),"%"
	return coverage

def net_cov(G,node,level,total):
	neigh = [] #neighbors of node
	trace = [] #to keep track of neighbors' recursion
	global cn
	global ct
	if(level==0):	
		return total
	else:
		for i in G.neighbors(node):
			neigh.append(i)
		for i in neigh:
			cn = cn+1
			if i not in total:
				trace.append(i)
				total.append(i)
		level=level-1
		if(len(trace)==0):
			return total
		for i in trace:
			total=net_cov(G,i,level,total)
	return total

def hubs_remove_len_one(G,asc):
	s = asc[0]
	sc=[]
	sc.append(s)
	for i in range(1,len(asc)):
		l = nx.shortest_path_length(G,asc[i],s)
		if(l>1):
			sc.append(asc[i])
	s = sc[1]
	sc1=[]
	sc1.append(s)
	for i in range(1,len(sc)):
		l = nx.shortest_path_length(G,sc[i],s)
		if(l>1):
			sc1.append(sc[i])
	return sc1
	
	
	
def openBinaries(filename):
	f = open(filename,"r")
	G = pickle.load(f)
	return G

def saveBinaries(G,filename):
	f = open(filename,"w")
	pickle.dump(G,f)
def plotgraph(title, dic1, dic2, xlabel, ylabel):
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(dic1.keys(),dic1.values(),'bo')
	plt.plot(dic2.keys(),dic2.values(),'go')
	plt.show()
def scalefree_graph(n, m):
    
	G=empty_graph(m)
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
def _random_subset(seq,m):
    
    print "Entered"
    targets=set()
    while len(targets)<m:
        x=random.choice(seq)
        targets.add(x)
    #print targets
    return targets


