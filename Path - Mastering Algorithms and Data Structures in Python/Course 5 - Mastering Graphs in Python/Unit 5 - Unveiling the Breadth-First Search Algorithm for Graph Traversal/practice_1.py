# Import the necessary libraries
from collections import deque

# Function for BFS traversal of the graph
def BFS_Traversal(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Double-ended queue to handle BFS operations

    print(f"The Breadth-First Search (BFS) traversal starting from node {start} is:")

    while queue:
        node = queue.popleft()  # Dequeue a node from the front
        print(node, end=" ")  # Print the visited node

        for neighbor in graph[node]:  # Check all neighbors
            if neighbor not in visited:  # If the neighbor has not been visited yet
                queue.append(neighbor)  # Enqueue the neighbor
                visited.add(neighbor)  # Mark the neighbor as visited

print()

# Use an adjacency list to represent the graph
graph = {'Start': ['Friend1', 'Friend2'], 'Friend1': ['Friend3', 'Friend5'],
         'Friend2': ['Friend4'], 'Friend3': ['Friend6'], 'Friend4': [],
         'Friend5': [], 'Friend6': []}

# Call the BFS_Traversal function
BFS_Traversal(graph, 'Start')
