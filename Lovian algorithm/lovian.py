import sys
sys.path.insert(0, '/home/shruthi/Documents/Projects/FYPFinal/Samata/')
import commonfunctions as cf
import networkx as NX
import networkx.readwrite.gml as NRG
import networkx.algorithms.centrality as NC
import pylab as P

def updateGraph(G):
    ebc = NC.edge_betweenness(G)
    maxs = 0
    medge = None
    for k, v in ebc.iteritems():
        if maxs < v:
            medge, maxs = k, v
    G.remove_edge(*medge)
    #return G

def drawGraph(G, pos, output):
    NX.draw(G, pos)
    P.savefig(output)
    P.draw()
    P.close()
    
def sort_dict(d):
	asc=[]
	for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
		asc.append(key)
	asc.reverse()
	return asc

#G = cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
G = cf.scalefree_graph(100,2)
#print G.nodes()
#cf.saveBinaries(G,"g.txt")
#G=cf.openBinaries("g.txt")
F = G.copy()
eNum = G.number_of_edges()
print "Number of edges in the graph",eNum
count=1
sub=[]
for i in range(80):
    #pos = NX.spring_layout(G)
    updateGraph(G)
	

#pos = NX.spring_layout(G)
#output = "greedy_img/graph.png"
#drawGraph(G, pos, output)
h = NX.connected_component_subgraphs(G)
"""
x = len(h)
print x
for i in range(x):
	pos = NX.spring_layout(h[i])
	output = "greedy_img/grpah%(id)02d.png" % {"id": i}
	drawGraph(h[i], pos, output)
"""
M = len(h) #9


influential_nodes = []

temp = []


print h[0].nodes()
#m=0
#print "number of communities",m
count = 0
influential = {}
for m in range(M):
	#print "value of m",m
	print h[m].nodes()
	deg = NX.degree_centrality(h[m])
	degs = sort_dict(deg)
	list_degs0 =[]
	list_degs1 =[]
	
	list_degs0.append(degs[0])
	list_degs1.append(degs[1])
	
	print "For community",m
	influential[degs[0]]=cf.network_coverage(h[m],list_degs0,2)
	#print influential
	influential[degs[1]]=cf.network_coverage(h[m],list_degs1,2)
	#print influential
sorted1=sort_dict(influential)
#print "unsorted",influential
#print "Sorted order",cf.top_e_log_n(sorted1,M)
print "---------------------------"
print "Network Coverage for lovian"
cnn=cf.network_coverage(F,cf.top_e_log_n(sorted1,M),2)
"""
s = cf.top_e_log_n(sorted1,M)[0]
ne=[]
ne.append(s)
for i in sorted1:
	l = NX.shortest_path_length(F,i,s)
	if(l>1):
		ne.append(i)
cnn=cf.network_coverage(F,ne,2)
"""
"""
influential1 = []
for m in range(M):
	total = []
	#print "value of m",m
	#print h[m].nodes()
	deg = NX.degree_centrality(h[m])
	degs = sort_dict(deg)
	influential1.append(degs[0])
	#total=cf.net_cov(F,degs[0],2,total)
	#print len(total)/100.0
"""	
#print len(influential1)
#print len(influential1)
#print "Network Coverage for old code"
#cnn=cf.network_coverage(F,cf.top_e_log_n(influential1,M),2)	

print "Degree"
cnd=cf.degreeRank(F,M)

overlapping_factor = (cnd-cnn)*100/(cnd*1.0)

print "Overlapping",overlapping_factor

		
	
	







