from hw0_util import *


if __name__ == '__main__':

    wikiGraph = extract_Graph( "Wiki-Vote.txt" )
    print("WikiGraph: Nodes %d, Edges %d" % (wikiGraph.GetNodes(), wikiGraph.GetEdges()))
    print("WikiGraph: %d Nodes have self-edges" % (count_self_edge(wikiGraph) ) )
    print("WikiGraph: has %d directed edges" % ( wikiGraph.GetEdges() - count_self_edge(wikiGraph) ) )
    print("WikiGraph: has %d undirected edges" % ( count_undirected_edges(wikiGraph) ) )
    print("WikiGraph: has %d reciprocated edges" % ( count_reciprocated_edges(wikiGraph) ) )
    print("WikiGraph: has %d zero out degree nodes" % ( zero_out_degree_node(wikiGraph) ) )
    print("WikiGraph: has %d zero in degree nodes" % ( zero_in_degree_node(wikiGraph) ) )
    print("WikiGraph: has %d nodes with more than %d in degree" % ( more_than_x_out_degree_node(wikiGraph,10), 10 ) )
    print("WikiGraph: has %d nodes with more than %d out degree" % ( more_than_x_in_degree_node(wikiGraph,10), 10 ) )