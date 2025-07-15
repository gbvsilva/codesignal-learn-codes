from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque()
    queue.append(root)

    level = {root: 0} # TODO: initialize levels dictionary

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        level_of_vertex = level[vertex] # TODO: set the current level of vertex

        for child in graph[vertex]:
            if child not in visited:
                queue.append(child)
                level[child] = level_of_vertex + 1 # TODO: set the level of the child

    print("\nTraversing completed!")
    return level

graph = {
  '1' : ['2', '3', '4'],
  '2' : ['5', '6'],
  '3' : ['7'],
  '4' : ['8', '9'],
  '5' : [],
  '6' : ['10'],
  '7' : ['11', '12'],
  '8' : [],
  '9' : [],
  '10' : [],
  '11' : [],
  '12' : []
}

print(BFS(graph, '1'))
