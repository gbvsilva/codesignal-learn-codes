# Import the necessary libraries
from collections import deque

def BFS_Traversal(graph, start):
    visited, queue = set(), deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(BFS_Traversal(graph, 'B'))
