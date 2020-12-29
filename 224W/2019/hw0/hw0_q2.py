from hw0_q1 import extract_Graph
import snap
import matplotlib.pyplot as plt 
import numpy as np
import math

def x_out_degree_node_classification(wikiGraph:snap.TNGraph):

    out_degree_map = {}
    min_x, max_x = 1, 0
    for node in wikiGraph.Nodes():
        if node.GetOutDeg() not in out_degree_map:
            out_degree_map[ node.GetOutDeg() ] = 0
        out_degree_map[ node.GetOutDeg() ] += 1
        min_x = min(node.GetOutDeg(), min_x )
        max_x = max(node.GetOutDeg(), max_x )
    return out_degree_map, min_x, max_x

wikiGraph = extract_Graph()

map, min_x, max_x = x_out_degree_node_classification(wikiGraph)
x = list(map.keys())
x.sort()   
y = [ map[i] for i in x ]


slope, intercept = np.polyfit( np.log10(np.array(x[1:])), np.log10(np.array(y[1:])), 1 )

print( " log y = %d * log x + %d" % ( slope, intercept ) )

linear_regressor_line = slope * np.log10(np.array(x[1:])) + intercept
plt.figure(figsize=(4, 3), dpi=70)
plt.loglog(x, y )
plt.loglog(x[1:], linear_regressor_line, '-')
plt.savefig("output.png", dpi=400)
plt.show()
