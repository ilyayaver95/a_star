import heapq

def astar(graph,start_node,end_node):
    # astar: F=G+H, we name F as f_distance, G as g_distance, 
    # H as heuristic
    f_distance={node:float('inf') for node in graph}
    f_distance[start_node]=0
    
    g_distance={node:float('inf') for node in graph}
    g_distance[start_node]=0
    
    came_from={node:None for node in graph}
    came_from[start_node]=start_node
    
    queue=[(0,start_node)]
    while queue:
        current_f_distance,current_node=heapq.heappop(queue)

        if current_node == end_node:
            print('found the end_node')
            return f_distance, came_from
        for next_node,weights in graph[current_node].items():
            temp_g_distance=g_distance[current_node]+weights[0]
            if temp_g_distance<g_distance[next_node]:
                g_distance[next_node]=temp_g_distance
                heuristic=weights[1]
                f_distance[next_node]=temp_g_distance+heuristic
                came_from[next_node]=current_node
                heapq.heappush(queue,(f_distance[next_node],next_node))
    return f_distance, came_from

if __name__ == "__main__":
    # list first value is the g-score, second value is the h-score,i.e., heuristic

     # first graph
    graph = {
        'S': {'A': [1.5, 2], 'D': [2, 4.5]},
        'A': {'B': [2, 2]},
        'B': {'C': [3, 4]},
        'C': {'F': [4, 0]},
        'D': {'E': [3, 2]},
        'E': {'F': [2, 0]},
        'F': {}
    }

    # second graph

    # # third graph
    # graph = {
    #     'S': {'B': [6, 8], 'F': [3, 6]},
    #     'B': {'C': [3, 5], 'D': [2, 7]},
    #     'D': {'E': [8, 3]},
    #     'G': {'I': [3, 1]},
    #     'C': {'E': [5, 3]},
    #     'E': {'J': [5, 0]},
    #     'F': {'H': [7, 3], 'G': [1, 5]},
    #     'H': {'I': [2, 1]},
    #     'I': {'J': [3, 0], 'E': [5, 3]},
    #     'J': {}}

    result = astar(graph, 'S', 'F')
    print(result)

