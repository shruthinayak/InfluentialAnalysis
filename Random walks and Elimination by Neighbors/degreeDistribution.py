import networkx as nx
import matplotlib.pyplot as plt
import pickle
def edgelists(n,path):
	f=open(path)
	f.readline()
	f.readline()
	f.readline()
	f.readline()

	edgelist=[]
	for i in range(0,n):
		
		line=f.readline()
		c=line.split("\t")
		s=c[0]
		l=c[1].split("\r\n")
		d=l[0]
		#edge.append(s)
		#edge.append(d)
		edge=(s,d)
		edgelist.append(edge)
	#print edgelist
	return edgelist

def createGraph(edgelist):
	G=nx.Graph()
	for i in edgelist:
		s=i[0]
		d=i[1]
		#print s,d
		if(G.has_node(s) and G.has_node(d)):
			G.add_edge(s,d)
		elif(G.has_node(s)):
			G.add_node(d)
			G.add_edge(s,d)
		elif(G.has_node(d)):
			G.add_node(s)
			G.add_edge(s,d)
		else:
			G.add_node(s)
			G.add_node(d)
			G.add_edge(s,d)
	return G

	
def plotdegree2(title, xlabel, ylabel,G):
	'''Degree v/s count'''
	degree={}
	fin={}
	n=G.nodes()
	for i in n:
		degree[i]=G.degree(i)
	val = degree.values()
	val.sort()
	while(len(val)!=0):
		cnt = val.count(val[0])
		fin[val[0]]=cnt
		for j in range(0,cnt):
			val.remove(val[0])
	print fin
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(fin.keys(),fin.values(),'bo')
	plt.show()
	
'''ed = edgelists(500,"/home/shruthi/Documents/Projects/SortedSNA/1RealWorldPattern/Soc/soc-Epinions1.txt")
G = nx.DiGraph()
G.add_edges_from(ed)
print "Graph Done"
nx.draw(G)
plt.show()
#G = createGraph(ed)
#plotdegree2(G)'''
filename = "/home/shruthi/Documents/Projects/FYPFinal/Binaries/collaboration.txt"
f = open(filename,"r")
G = pickle.load(f)
print (2*G.number_of_edges())/(1.0*G.order()*(G.order()-1))
plotdegree2("Collaboration", "Degree", "Count", G)
