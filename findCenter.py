# 1791. Find Center of Star Graph
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# 
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
# 
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

#solution# 1

def findCenter (edges):
    searchItem1 = edges[0][0]
    searchItem2 = edges[0][1]
    result = []
    for i in range(1, len(edges)):
        if searchItem1 == edges[i][0] or searchItem1 == edges[i][1]:
            result. append(searchItem1)
        elif searchItem2 == edges[i][0] or searchItem2 == edges[i][1]:
            result.append(searchItem2)
    if result == [searchItem1] * (len(edges)-1):
        return (searchItem1)
    elif result == [searchItem2] * (len(edges)-1):
        return (searchItem2)    
    
#solution 2 - shorter

def findCenter (edges):
    if edges[0][0] != edges[1][0] and edges[0][0] != edges[1][1]:
        return edges[0][1]
    else:
        return edges[0][0]

#testing
edges = [[1,2],[5,1],[1,3],[1,4]]
findCenter (edges)

edges = [[1,2],[2,3],[4,2]]
findCenter(edges)
