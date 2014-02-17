import math
from random import choice
import networkx as nx
import pickle
import time
level=2
def top_e_log_n(hotspots,n):
	hubs=[]
	
	#m=math.e*math.log(n)
	#m= int (m)
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
	#print "Similar nodes:",sim_nodes
	print "Num of sim nodes: ",count
	return sim_nodes
def degreeRank(G,n):
	ts = time.time()
	deg = nx.degree_centrality(G)
	
	degs=sort_dict(deg)
	te=time.time()
	asc = top_e_log_n(degs,n)
	#print "Degree order:",asc
	asc = network_coverage1(G,asc,level)
	
	print "Time taken for Degree:",round(te-ts,2)
	return degs
def degreeRankCommunity(G,n,comm):
	ts = time.time()
	deg = nx.degree_centrality(G)
	degs=sort_dict(deg)
	asc = top_e_log_n(degs,n)
	print "Degree order:",asc
	asc = network_coverage(G,asc,level)
	te=time.time()
	print "Time taken for Degree:",round(te-ts,2)
	output = []
	for x in deg:
		if x not in output:
			output.append(x)
			#print output
	return output
def betweenessRank(G,n):
	ts = time.time()
	bet = nx.betweenness_centrality(G)
	bets=sort_dict(bet)
	asc = top_e_log_n(bets,n)
	asc = network_coverage(G,asc,level)
	te=time.time()
	print "Time taken for Betweeness:",te-ts
	return bets

def eigenvectorRank(G,n):
	ts = time.time()
	bet = nx.eigenvector_centrality(G)
	bets=sort_dict(bet)
	asc = top_e_log_n(bets,n)
	asc = network_coverage(G,asc,level)
	te=time.time()
	print "Time taken for Eigen:",te-ts
	return bets
def degreeRankHubs(G,hubs):
	degs = degreeRank(G)
	rank=[]
	for i in degs:
		if i in hubs:
			rank.append(i)
	return rank
	
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
	
def network_coverage(G,hubs,level):
	
	coverage=0
	count=0
	graph={}
	total=[]
	n=G.number_of_nodes()
	for i in hubs:
		if (coverage==1.0):
			count+=1
			print "With node : ",i , " Network coverage = ",coverage
			break
		else:
			count=count+1
			total = net_cov(G,i,level,total)
			coverage = round(len(total)/(n*1.0),3)
			
			if(coverage not in graph.values()):
				graph[i]=coverage
	print "Network coverage = ",(coverage*100),"%"
	asc=sort_dict(graph)
	asc.reverse()
	
	#print len(asc)
	return asc
	
def network_coverage1(G,hubs,level):
	
	coverage=0
	count=0
	graph={}
	total=[]
	n=G.number_of_nodes()
	for i in hubs:
		if (coverage==1.0):
			count+=1
			#print "With node : ",i , " Network coverage = ",coverage
			break
		else:
			count=count+1
			total = net_cov(G,i,level,total)
			coverage = round(len(total)/(n*1.0),3)
			#print "With node : ",i , " Network coverage = ",coverage	
	print "With hubs:",count
	print "Coverage: ",coverage
	asc=sort_dict(graph)
	asc.reverse()
	#print asc
	return asc
	
def net_cov(G,node,level,total):
	neigh = []
	trace = [] 
	
	if(level==0):	
		return total
	else:
		for i in G.neighbors(node):
			neigh.append(i)
		for i in neigh:
			if i not in total:
				trace.append(i)
				total.append(i)
		level=level-1
		if(len(trace)==0):
			return total
		for i in trace:
			total=net_cov(G,i,level,total)
	return total
	
def openBinaries(filename):
	f = open(filename,"r")
	G = pickle.load(f)
	return G

def saveBinaries(G,filename):
	f = open(filename,"w")
	pickle.dump(G,f)
	
