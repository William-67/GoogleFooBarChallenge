from collections import deque

def bfs(graph, parent, source, sink):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True

    return visited[sink]

def max_flow(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, parent, source, sink):
        path_flow = float("inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

def solution(entrances, exits, path):
    num_rooms = len(path)
    source = num_rooms
    sink = num_rooms + 1

    # Create a graph with source and sink nodes
    graph = [[0] * (num_rooms + 2) for _ in range(num_rooms + 2)]

    # Connect entrances to source and exits to sink with infinite capacity
    for entrance in entrances:
        graph[source][entrance] = float("inf")
    for exit in exits:
        graph[exit][sink] = float("inf")

    # Copy the path capacities to the graph
    for i in range(num_rooms):
        for j in range(num_rooms):
            graph[i][j] = path[i][j]

    max_flow_result = max_flow(graph, source, sink)
    return max_flow_result

# Test cases
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))  # Output: 6
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))  # Output: 16
