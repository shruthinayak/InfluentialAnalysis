import matplotlib.pyplot as plt

plt.figure()
plt.title("Comparitive analysis: Cardinality of Influential Node Set v/s Network Coverage - Collaboration Network")
#Degree
plt.plot([100,200,300,400,500,600,700,800,900,1000],[26.1,26.1,36.8,42.3,47.0,47.8,51.6,54.1,57.0,59.9],'ro-',linewidth=3.0,markersize=5.0)
#Random-Walks
plt.plot([100,200,300,400,500,600,700,800,900,1000],[51.3,60.7,66.1,69.5,71.8,74.3,76.2,77.7,79.0,80.4],'bo-',linewidth=3.0,markersize=5.0)
#Elimination 
plt.plot([100,200,300,400,500,600,700,800,900,1000],[60.4,67.7,72.3,75.9,78.4,80.8,82.5,84.1,85.8,87.5],'go-',linewidth=3.0,markersize=5.0)




plt.legend(['Degree','RandomWalks','EliminationByNeighbors'],loc=2)
plt.xlabel('Cardinality')
plt.ylabel('Network Coverage')
plt.axis([100, 1000, 25, 95])
plt.grid()
plt.show()
plt.close()
