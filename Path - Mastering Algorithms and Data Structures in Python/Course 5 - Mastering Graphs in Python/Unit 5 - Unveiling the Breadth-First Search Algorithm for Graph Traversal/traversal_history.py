from collections import deque

def BFS(graph, start):
    visited, queue = set([start]), deque([start]) # initialize BFS starting state
    traversal_history = []

    while queue:
        vertex = queue.popleft()
        traversal_history.append(vertex)

        # TODO: process vertex's neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_history

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['F', 'G'],
    'C': ['H', 'I'],
    'D': ['J'],
    'F': [],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': ['M', 'N'],
    'M': [],
    'N': []
}

print(BFS(graph, 'C'))
