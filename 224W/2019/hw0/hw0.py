try:
    import snap
    version = snap.Version
    print("SUCCESS, your version of Snap.py is %s" % (version))
except:
    pass

def extract_Graph():

    wikiGraph = snap.TNGraph.New()
    f = open("Wiki-Vote.txt", "r")
    nodes = set()
    
    for x in f.readlines():
        if x.startswith("#"):
            continue
        from_node, to_node = map(int, x.split())
        
        if from_node not in nodes:
            nodes.add( from_node )
            wikiGraph.AddNode( from_node )
        if to_node not in nodes:
            nodes.add( to_node )
            wikiGraph.AddNode( to_node )

        wikiGraph.AddEdge( from_node, to_node )
    f.close()
    return wikiGraph

def count_self_edge(wikiGraph:snap.TNGraph) -> (int):

    count = 0
    for node in wikiGraph.Nodes():
        if wikiGraph.IsEdge( node.GetId(), node.GetId() ):
            count += 1
    return count
    
def determineKeyOfEdge( edge ) -> (str,int):
    if edge.GetSrcNId() > edge.GetDstNId():
        return str(edge.GetDstNId()) + "_" + str(edge.GetSrcNId()),-1
    return str(edge.GetSrcNId()) + "_" + str(edge.GetDstNId()),1
    

def count_undirected_edges(wikiGraph:snap.TNGraph) -> (int):

    countUndirected = 0
    discovered_edge_set = set()
    for edge in wikiGraph.Edges():

        if edge.GetDstNId() == edge.GetSrcNId() :
            continue

        edge_key, _ = determineKeyOfEdge( edge )
        if edge_key not in discovered_edge_set:
            discovered_edge_set.add( edge_key )
            countUndirected += 1

    return countUndirected

def count_reciprocated_edges(wikiGraph:snap.TNGraph) -> (int):

    count_reciprocated = 0
    discovered_edge_map = {}
    for edge in wikiGraph.Edges():
        
        if edge.GetDstNId() == edge.GetSrcNId() :
            continue

        edge_key, edge_direction = determineKeyOfEdge( edge )
        if edge_key not in discovered_edge_map :
            discovered_edge_map[ edge_key ] = 0
        discovered_edge_map[ edge_key ] += edge_direction

    for val in discovered_edge_map.values():
        if val == 0:
            count_reciprocated += 1
    return count_reciprocated 


wikiGraph = extract_Graph()
print("WikiGraph: Nodes %d, Edges %d" % (wikiGraph.GetNodes(), wikiGraph.GetEdges()))
print("WikiGraph: %d Nodes have self-edges" % (count_self_edge(wikiGraph) ) )
print("WikiGraph: has %d directed edges" % ( wikiGraph.GetEdges() - count_self_edge(wikiGraph) ) )
print("WikiGraph: has %d undirected edges" % ( count_undirected_edges(wikiGraph) ) )
print("WikiGraph: has %d reciprocated edges" % ( count_reciprocated_edges(wikiGraph) ) )