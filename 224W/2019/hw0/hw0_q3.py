from hw0_util import extract_Graph
import snap



if __name__ == '__main__':

    stackOverflowGraph = extract_Graph( "stackoverflow-Java.txt" )

    Components = snap.TCnComV()
    snap.GetWccs(stackOverflowGraph, Components)
    print( "Total Number of Weakly Connected Components: %d"%len( Components ) )

    MaxWeaklyConnComp = snap.GetMxWcc(stackOverflowGraph)

    print( "Edges in Largest Weakly Connected Component: %d"% MaxWeaklyConnComp.GetEdges() )
    print( "Nodes in Largest Weakly Connected Components: %d"% MaxWeaklyConnComp.GetNodes() )


    print( "Central Nodes according to PageRank" )
    PRankH = snap.TIntFltH()
    snap.GetPageRank(stackOverflowGraph, PRankH)

    PRankH.SortByDat(False)
    i = 1
    for nodeId in PRankH:
        if i > 3:
            break
        i += 1
        print( "Node: %d Rank: %f"%(nodeId, PRankH[nodeId]) )

    print( "Central Nodes according to HITS" )
    NodeIDHubH = snap.TIntFltH()
    NodeIDAuthH = snap.TIntFltH()

    snap.GetHits(stackOverflowGraph, NodeIDHubH, NodeIDAuthH)

    print("By Authorities")
    NodeIDAuthH.SortByDat(False)
    i = 1
    for nodeId in NodeIDAuthH:
        if i > 3:
            break
        i += 1
        print( "Node: %d Rank: %f"%(nodeId, NodeIDAuthH[nodeId]) )

    print("By Hubs")
    NodeIDHubH.SortByDat(False)
    i = 1
    for nodeId in NodeIDHubH:
        if i > 3:
            break
        i += 1
        print( "Node: %d Rank: %f"%(nodeId, NodeIDHubH[nodeId]) )
    
