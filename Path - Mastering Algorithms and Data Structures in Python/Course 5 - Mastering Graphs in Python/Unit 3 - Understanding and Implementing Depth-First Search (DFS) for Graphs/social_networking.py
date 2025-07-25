# Define a graph using dictionary
graph = {
    'Alice': set(['Carol', 'David']),
    'Bob': set(['Alice', 'Eve']),
    'Carol': set(['Alice', 'Eve']),
    'David': set(['Alice']),
    'Eve': set(['Bob','Carol']),
}

def DFS(graph, start_node, visited):
    """
    Function to implement DFS for the graph.
    """
    if start_node in visited:
        return

    visited.add(start_node)
    print(start_node, end=' --> ')

    for neighbour in graph[start_node]:
        if neighbour not in visited:
            DFS(graph, neighbour, visited)

visited = set()
# Call our DFS function, starting with 'Alice'
DFS(graph, 'Bob', visited)  # Depicts the DFS traversal. It could vary basis the order in which neighbors are processed.
print('\nVisited nodes:', visited)
