import matplotlib.pyplot as plt
import networkx as nx
from random import choice
import math
import random
import time
import sys
sys.path.insert(0, '/home/shruthi/Documents/Projects/SortedSNA')
import commonfunctions as cf

def meet_hotspot(G):
	count=0
	encounter=0
	nodes = G.nodes()
	d={}
	for i in nodes:
		d[i]=0
	ts = time.time()
	while(d[cf.sort_dict(d)[0]]<20):
		print d[cf.sort_dict(d)[0]]
		count=count+1
		#print count
		current=choice(G.nodes())
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
			if(trial==4):
				break;
			current=nextnode
			pathlen=pathlen+1
		for node in path:
			d[node]=d[node]+1
	#print dic
	te=time.time()
	print "Time taken:",round(te-ts,2)
	print count
	asc = cf.sort_dict(d)
	return asc
	
def hubs_immediate_neighbors(G,asc):
	'''count=0
	while(count<2):
		
			
	
		s = asc[count]
		sc=[]
		sc.append(s)
		for i in range(1,len(asc)):
			l = nx.shortest_path_length(G,asc[i],s)
			if(l>2):
				sc.append(asc[i])
		asc=sc
		count=count+1'''
	
	for i in range(0,1):
		node=asc[i]
		total=[]
		total = cf.net_cov(G,node,1,total)
		for i in total:
			if i in asc:
				asc.remove(i)
		return asc

G=cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/collaboration.txt")
#G=cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
#G=cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/soc.txt")
asc = meet_hotspot(G)
#nx.draw(G)
#plt.show()
#print cf.top_e_log_n(asc,10)
deg = nx.degree_centrality(G)
d = cf.sort_dict(deg)

for h in range(100,1100,100):
	s = cf.top_e_log_n(asc,h)
	cnr = cf.network_coverage(G,s,2)
	s = cf.top_e_log_n(d,h)
	cnd = cf.network_coverage(G,s,2)

#print (cnd-cnr)*100/(cnd*1.0)
