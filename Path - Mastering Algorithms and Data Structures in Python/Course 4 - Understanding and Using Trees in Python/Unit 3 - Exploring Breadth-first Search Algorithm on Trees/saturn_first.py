from collections import deque

# Representing the tree as an adjacency list
graph = {
  'Mars' : ['Jupiter', 'Saturn'],
  'Jupiter' : ['Mars', 'Neptune', 'Uranus'],
  'Saturn' : ['Mars', 'Venus', 'Mercury'],
  'Neptune' : ['Jupiter'],
  'Uranus' : ['Jupiter', 'Earth'],
  'Venus' : ['Saturn'],
  'Mercury' : ['Saturn'],
  'Earth' : ['Uranus']
}

# BFS Function
def BFS(graph, root):
    visited = [] # List to keep track of visited nodes
    queue = deque()
    queue.append(root) # Start with the root node

    while queue: # While there are nodes to visit.
        vertex = queue.popleft() # Visit the first node in the queue
        print(f"{vertex} has been visited")
        visited.append(vertex) # Add it to the visited nodes list

        for neighbour in graph[vertex]: # Add all unvisited children to the queue
            if neighbour not in visited:
                queue.append(neighbour)
    return visited

print("\nOrder of visited planets: ", BFS(graph, 'Saturn')) # Start at Mars
