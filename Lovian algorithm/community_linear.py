import sys
sys.path.insert(0, '/home/shruthi/Documents/Projects/FYPFinal/Samata/')
import commonfunctions as cf
import random
import itertools
import networkx as nx
import time

import Orange.core
import Orange.data


def add_results_to_items(G, lblhistory):
    items = G.items()
   
    attrs = [Orange.feature.Discrete('clustering label propagation',
                            values=list(set([l for l in lblhistory[-1]])))]

    dom = Orange.data.Domain(attrs, 0)
    data = Orange.data.Table(dom, [[l] for l in lblhistory[-1]])

    if items is None:
        G.set_items(data)
    else:
        G.set_items(Orange.data.Table([items, data]))


def add_history_to_items(G, lblhistory):
    items = G.items()
    
    attrs = [Orange.feature.Discrete('c' + str(i), values=list(set(\
            [l for l in lblhistory[0]]))) for i, _ in enumerate(lblhistory)]

    dom = Orange.data.Domain(attrs, 0)
    data = map(list, zip(*lblhistory))
    data = Orange.data.Table(dom, data)
    if items is None:
        G.set_items(data)
    else:
        G.set_items(Orange.data.Table([items, data]))



def label_propagation(G, results2items=0, \
                      resultHistory2items=0, iterations=1000):
  
    vertices = sorted(G.nodes_iter())
    labels = dict(zip(vertices, range(G.number_of_nodes())))
    #print labels

    def next_label(neighbors):
        
        lbls = sorted(labels[u] for u in neighbors)
        lbls = [(len(list(c)), l) for l, c in itertools.groupby(lbls)]
        m = max(lbls)[0]
        return [l for c, l in lbls if c >= m]

    lblhistory = []
    for i in range(iterations):
        random.shuffle(vertices)
        stop = 1
        for v in vertices:
            nbh = G.neighbors(v)
            if len(nbh) == 0:
                continue

            max_lbls = next_label(nbh)

            if labels[v] not in max_lbls:
                stop = 0

            labels[v] = random.choice(max_lbls)

        lblhistory.append([str(labels[key]) for key in sorted(labels.keys())])

        if stop:
            for v in vertices:
                nbh = G.neighbors(v)
                if len(nbh) == 0:
                    continue
                max_lbls = next_label(nbh)
                if labels[v] not in max_lbls:
                    stop = 0
                    break

            if stop:
                break

    if results2items and not resultHistory2items:
        add_results_to_items(G, lblhistory)

    if resultHistory2items:
        add_history_to_items(G, lblhistory)

    print "iterations:", i
    #print labels
    return labels
    
G = cf.openBinaries("/home/shruthi/Documents/Projects/FYPFinal/Binaries/gnutella.txt")
#G = nx.read_gpickle("/home/samata/Samata/8th_sem_proj/data/email.gpickle")
#G = cf.scalefree_graph(100,2)
ts = time.time()
label_result = label_propagation(G)

label_result = sorted(label_result.items(), key=lambda x:x[1])

groups = itertools.groupby(label_result, key=lambda x:x[1])

remainder = []
matched   = []

for key, group in groups:
   group = list(group)
   if len(group) == 1:
      remainder.append( group[0] )
   else:
      matched.append( dict(group) )
else:
   remainder = dict(remainder)
   
#print "Remainder",remainder
#print "Matched",matched

hubs=[]
x=len(matched[-1])
for m in matched:
	comm_deg = m.keys()
	deg={}
	for i in comm_deg:
		deg[i]=G.degree(i)
	asc=cf.sort_dict(deg)
	x=int(0.1*len(asc))
	if(x<1):
		x=1
	asc=cf.top_e_log_n(asc,x)
	for i in asc:
		hubs.append(i)
#print hubs,len(hubs)
te=time.time()
print "Time taken for community + influential nodes:",round(te-ts,2)
print len(hubs)
cnn=cf.network_coverage(G,hubs,2)

print "Network Coverage Degree"
cnd = cf.degreeRank(G,817)

overlapping_factor = (cnd-cnn)*100/(cnd*1.0)

print "Overlapping",overlapping_factor

