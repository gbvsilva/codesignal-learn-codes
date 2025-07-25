# Import necessary libraries
from collections import deque

def BFS(graph, start_node):
    # Create an empty set for visited nodes and a queue for BFS
    queue = deque([start_node])
    visited = set([start_node])

    print(f"The BFS traversal, starting at node {start_node}, displays nodes in this order: ")

    # Loop until the queue is empty
    while queue:
        node = queue.popleft()  # Remove a node from the front of the queue
        print(node, end=" ")  # Print the visited node

        for neighbor in graph[node]:  # Visit all the node's neighbors
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Enqueue the neighbor

print()

# Graph representation as an adjacency list
graph = {
    'Earth': ['Mars', 'Jupiter'],
    'Mars': ['Neptune', 'Pluto'],
    'Jupiter': ['Venus', 'Saturn'],
    'Neptune': [],
    'Pluto': [],
    'Venus': ['Uranus'],
    'Saturn': [],
    'Uranus': []
}

# Initiate BFS traversal starting from 'Earth'
BFS(graph, 'Earth')
