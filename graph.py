import matplotlib.pyplot as plt

plt.figure()
plt.title("Comparitive analysis: Cardinality of Influential Node Set v/s Network Coverage")
#Degree
plt.plot([100,200,300,400,500,600,700,800,900,1000],[49.7,58.7,63.5,67,69.9,71.8,74,75.9,77.5,79.2],'ro-',linewidth=3.0,markersize=5.0)
#Betweeness
plt.plot([100,200,300,400,500,600,700,800,900,1000],[54.3,59.2,64.0,68.2,71.0,73.7,76.4,78.9,80.7,82.5],'bo-',linewidth=3.0,markersize=5.0)
#Label Propogation
plt.plot([100,200,300,400,500,600,700,800,900,1000],[47.6,58.0,63.1,66.8,69.8,71.7,73.9,75.9,77.4,79.1],'go-',linewidth=3.0,markersize=5.0)
#Local-Centrality
plt.plot([100,200,300,400,500,600,700,800,900,1000],[33.5,39.7,45.3,48.8,53.9,59.2,61.1,62.8,65.1,67.4],'co-',linewidth=3.0,markersize=5.0)
#Random-Walks
plt.plot([100,200,300,400,500,600,700,800,900,1000],[49.7,62.2,66.6,71.0,74.9,78.1,80.5,82.6,84.9,86.5],'ko-',linewidth=3.0,markersize=5.0)
#Elimination By Neighbors
plt.plot([100,200,300],[57.8,65.7,68.2],'mo-',linewidth=3.0,markersize=5.0)
plt.legend(['Degree','Betweenness','Label-Propagation','Local-Centrality','RandomWalks','EliminationByNeighbors'],loc=2)
plt.xlabel('Cardinality')
plt.ylabel('Network Coverage')
plt.axis([100, 1000, 30, 90])
plt.grid()
plt.show()
plt.close()
