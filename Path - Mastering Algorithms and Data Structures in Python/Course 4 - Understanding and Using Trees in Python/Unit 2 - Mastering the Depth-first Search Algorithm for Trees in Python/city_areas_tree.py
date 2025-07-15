class Area:
    def __init__(self, name):
        self.name = name
        self.subareas = []

    # TODO: Define the add_subarea method to add a subarea to a given area
    def add_subarea(self, name):
        self.subareas.append(Area(name))

    # TODO: Define the dfs_traversal method to perform a depth-first search traversal over the areas
    def dfs_traversal(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self.name)
        print(self.name)
        for area in self.subareas:
            if area.name not in visited:
                area.dfs_traversal(visited)

# TODO: Construct a tree to represent areas of a city
city = Area('Campo Grande')
city.add_subarea('Centro')
centro = city.subareas[0]
centro.add_subarea('Igreja Matriz de Santana')
city.add_subarea('Alto da Capela')
alto_da_capela = city.subareas[1]
alto_da_capela.add_subarea('Capelinha')
city.add_subarea('Alto da Esperança')

# TODO: Conduct a DFS traversal to print all areas
print('City traversal:')
city.dfs_traversal()
