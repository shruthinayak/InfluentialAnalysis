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
	
	for t in range(10,90,10):
		ts = time.time()
		while(d[cf.sort_dict(d)[0]]<t):
			#print d[cf.sort_dict(d)[0]]
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
		#print "Time taken:",round(te-ts,2)
		#print count
		asc = cf.sort_dict(d)
		print t
	
		s = cf.top_e_log_n(asc,1200)
		
		cnr = cf.network_coverage(G,s,2)

	return asc


G=cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
asc = meet_hotspot(G)
