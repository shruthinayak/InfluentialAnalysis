import networkx as nx
import matplotlib.pyplot as plt
import itertools
import commonfunctions as cf
""" Reading the graph from the file-- # is the comment--\t the separator """ 
#G=nx.read_adjlist("p2p-Gnutella09.txt","#","\t",nodetype=int) 
""" read from the stored constructed graph"""
G = cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
#G=nx.barabasi_albert_graph(100,2)
print G.nodes(),"these are the nodes"
print "NUmber of nodes",G.number_of_nodes() #8114
print "NUmber of nodes",G.number_of_edges() #26013
"""H=nx.connected_component_subgraphs(G)[-1]
print H.nodes()
nx.draw(H)
plt.show()"""
#print nx.average_shortest_path_length(G)
#print nx.shortest_path_length(G,8111,2885)
""" To find the sum of all shortest paths"""
distance1=0 
distance2=0
distance3=0
"""No.of nodes"""
n=G.order()
first=n/3
sec=2*n/3 
count=0

if(nx.is_directed(G)):
	print "directed"
	print first,sec,n
	fi=G.nodes()[0:first]
	se=G.nodes()[first:sec]
	th=G.nodes()[sec:n]
	print "size f=",len(fi)
	print "------------------------------------------------------------"
	print "s=",len(se)
	print "------------------------------------------------------------"
	print "t=",len(th)
	print "-------------------------------------------------------------"
	
	for x,y,z in itertools.izip(fi,se,th):
		for i in G.nodes():
			u=v=w=i
			f=nx.has_path(G,x,u)
			s=nx.has_path(G,y,v)
			t=nx.has_path(G,z,w)
			print "node is",x,u
			print "node is",y,v
			print "node is",z,w
			if f and s and t:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				count=count+3
				print "Alll true "
			elif f and s:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				print "FIRST 2 TRUE"
				count=count+2
			elif s and t:
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				print "SECONG 2 TRUE"
				count=count+2
			elif f and t:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				print "EXTREME 2 TRUE"
				count=count+2
			else:
				print "no path"
	print "done with different loop condition cause directed graph gives error if a node is not present"
	
else:
	for x,y,z in itertools.izip(range(0,first),range(first,sec),range(sec,n)):
		for u,v,w in itertools.izip(range(x+1,n),range(y+1,n),range(z+1,n)):
		
			f=nx.has_path(G,x,u)
			s=nx.has_path(G,y,v)
			t=nx.has_path(G,z,w)
			if f and s and t:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				count=count+3
				print "Alll true "
			elif f and s:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				print "FIRST 2 TRUE"
				count=count+2
			elif s and t:
				length2=nx.shortest_path_length(G,y,v)
				distance2=distance2+length2
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				print "SECONG 2 TRUE"
				count=count+2
			elif f and t:
				length1=nx.shortest_path_length(G,x,u)
				distance1=distance1+length1
				length3=nx.shortest_path_length(G,z,w)
				distance3=distance3+length3
				print "EXTREME 2 TRUE"
				count=count+2
			else:
				print "no path"
				
distance=distance1+distance2+distance3
print "distance",distance
denominator=n*(n-1)
print "n=",n
print "denominator",denominator
print count
avg=float(distance)/count

print "AVERAGE PATH LENGTH",avg

# AVERAGE PATH LENGTH 4.74774201447 for gnutella graph
	
	

