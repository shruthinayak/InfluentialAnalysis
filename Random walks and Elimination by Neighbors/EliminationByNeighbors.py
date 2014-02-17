import matplotlib.pyplot as plt
import networkx as nx
from random import choice
import math
import random
import time
import sys
import networkx as nx
import matplotlib.pyplot as plt
sys.path.insert(0, '/home/shruthi/Documents/Projects/SortedSNA')
import commonfunctions as cf
import pickle

def elimination(G):
	print "Entered"
	F = G.copy()
	hubs=[]
	while(G.number_of_edges()!=0):
		#print G.order()
		deg = nx.degree_centrality(G)
		asc = cf.sort_dict(deg)
		
		maxx=[]
		for i in range(0,5):
			total=[]
			total = cf.net_cov(G,asc[i],2,total)
		
			if(len(total)>len(maxx)):
				maxx=total
				
				hub = asc[i]
				maxx.append(hub)
				
		hubs.append(hub)
		for i in maxx:
			if i in G.nodes():
				G.remove_node(i)
	
	#print "Current number of nodes:",G.order()
	'''
	for i in G.nodes():
		deg[i]=F.degree(i)
	asc = cf.sort_dict(deg)
	for i in range(0,505):
		hubs.append(asc[i])
	'''
	return hubs

#G = nx.read_edgelist("/home/shruthi/Documents/Projects/SortedSNA/1RealWorldPattern/CollaborationNetwork/CA-HepPh.txt","#","\t",nodetype=int)
#cf.saveBinaries(G,"/home/shruthi/Documents/Projects/FYPFinal/Binaries/collaboration.txt")
G=cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
print "Loading Done.."
F = G.copy()

ts = time.time()
hubs = elimination(G)
te=time.time()
print "Time:",round(te-ts,2)
d = nx.degree_centrality(F)
asc = cf.sort_dict(d)
print len(hubs)
#print hubs
for h in range(100,1100,100):
	print h
	print "Elimination"
	cnn = cf.network_coverage(F,cf.top_e_log_n(hubs,h),2)
	print "Degree"
	cnn = cf.network_coverage(F,cf.top_e_log_n(asc,h),2)
#print cf.distance(F,hubs)
'''print cnn
cnd = cf.degreeRank(F,len(hubs))
print cnd
overlapping_factor = (cnd-cnn)*100/(cnd*1.0)
print "Overlapping factor:",overlapping_factor
'''
