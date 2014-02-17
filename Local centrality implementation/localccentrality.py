import networkx as nx
import random
import itertools

import threading

import commonfunctions as cf
import time
import matplotlib.pyplot as plt

#G=cf.scalefree_graph(100,2)
#G=nx.read_gpickle("/media/Patrick/8th sem/project/code/data/gnutella.gpickle")
#nx.draw(G)
#plt.show()
G = cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
def calculateN(G):
	n={}
	for nodes in G.nodes():
		count=0
		neigh=[]
		neigh=G.neighbors(nodes)
		count=G.degree(nodes)
		for i in neigh:
			count=count+G.degree(i)	
		n[nodes]=count
	return n
	
def calculateQ(G,N):
	q={}
	for nodes in G.nodes():
		
		count=0
		for i in G.neighbors(nodes):
			count=count+N[i]
		q[nodes]=count
	return q

def localcentrality(G,q):
	l={}
	for nodes in G.nodes():
		
		count=0
		for i in G.neighbors(nodes):
			count=count+q[i]
		l[nodes]=count
	return l
	
N={}
Q={}
L={}
N=calculateN(G)
Q=calculateQ(G,N)
te=time.time()
L=localcentrality(G,Q)
#print "ranking",L

nodes=[]
for key in sorted(L.iteritems(),key=lambda b:b[1],reverse=True):
	nodes.append(key[0])
ts=time.time()
print "TIME FOR LOCALCENTRALITY",round((ts-te),2)
#print "sorted accroding to localcentrality",nodes
#print "LOCAL"
cnn=cf.network_coverage(G,cf.top_e_log_n(nodes,285),2)
print "DEGREE"
ctt=cf.degreeRank(G,285)
print "Overlapping factor",(ctt-cnn)*100/(ctt*1.0)
