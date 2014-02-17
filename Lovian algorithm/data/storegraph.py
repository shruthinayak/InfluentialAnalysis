import networkx as nx
"""
# Reading the graph from the file-- # is the comment--\t the separator  
G=nx.read_adjlist("/media/Patrick/8th sem/project/code/gnutella/p2p-Gnutella09.txt","#","\t",nodetype=int) 
nx.write_gpickle(G,"/media/Patrick/8th sem/project/code/data/gnutella.gpickle")

#To read graphml file
G=nx.read_graphml("airlines.graphml",int)
nx.write_gpickle(G,"/media/Patrick/8th sem/project/code/data/gnutella.gpickle")




#Reading the graph from the file-- # is the comment--\t the separator-DIRECTED GRAPH 
G=nx.read_edgelist("/media/Patrick/8th sem/project/code/facebook/soc-Epinions1.txt","#","\t",create_using=nx.DiGraph(),nodetype=int)
nx.write_gpickle(G,"/media/Patrick/8th sem/project/code/data/epinions.gpickle")
"""
# Reading the graph from the file-- # is the comment--\t the separator  
G=nx.read_adjlist("/media/Patrick/8th sem/project/code/email/Email-Enron.txt","#","\t",nodetype=int) 
nx.write_gpickle(G,"/media/Patrick/8th sem/project/code/data/email.gpickle")
