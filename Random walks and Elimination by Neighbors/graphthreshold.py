import matplotlib.pyplot as plt

plt.figure()
plt.title("Threshold Analysis")
#800 hubs
plt.plot([10,20,30,40,50,60,70,80],[76.6,79.2,80.1,80.7,81.9,82.5,83.1,83.6],'ro-',linewidth=3.0,markersize=5.0)
#400 hubs
plt.plot([10,20,30,40,50,60,70,80],[63.9,68.3,70.1,69.6,70.8,70.7,70.8,70.7],'bo-',linewidth=3.0,markersize=5.0)
#=600
plt.plot([10,20,30,40,50,60,70,80],[71.7,75.6,76.8,77.1,77.7,79.2,78.8,78.9],'go-',linewidth=3.0,markersize=5.0)
#1000
plt.plot([10,20,30,40,50,60,70,80],[77.7,78.7,81.9,84.0,85.1,85.3,85.9,86.2],'co-',linewidth=3.0,markersize=5.0)
#1200
plt.plot([10,20,30,40,50,60,70,80],[76.8,84.0,85.3,86.4,87.5,88.6,88.5,89.2],'mo-',linewidth=3.0,markersize=5.0)

#Degree 
plt.plot([10],[68.2],'bo',linewidth=3.0,markersize=10.0)
plt.plot([10],[71.0],'go',linewidth=3.0,markersize=10.0)
plt.plot([10],[78.9],'ro',linewidth=3.0,markersize=10.0)
plt.plot([10],[82.5],'co',linewidth=3.0,markersize=10.0)


#Random-Walks
#plt.plot([100,200,300,400,500,600,700,800,900,1000],[49.7,62.2,66.6,71.0,74.9,78.1,80.5,82.6,84.9,86.5],'ko-',linewidth=3.0,markersize=5.0)
#Elimination By Neighbors
#plt.plot([100,200,300],[57.8,65.7,68.2],'mo-',linewidth=3.0,markersize=5.0)
#plt.legend(['Degree','Betweenness','Label-Propagation','Local-Centrality','RandomWalks','EliminationByNeighbors'],loc=2)
#plt.xlabel('Cardinality')
#plt.ylabel('Network Coverage')
plt.axis([10, 80, 60, 100])
plt.grid()
plt.show()
plt.close()
