# Defining an empty dictionary to represent the Adjacency List of our graph
city_connections = {}

# Adding vertices to graph by adding keys to dictionary
city_connections["Boston Library"] = []
city_connections["Fenway Park"] = []
city_connections["Quincy Market"] = []

# Adding an edge between two vertices
city_connections["Fenway Park"].append("Boston Library")

# Adding more edges
city_connections["Fenway Park"].append("Quincy Market")
city_connections["Boston Library"].append("Quincy Market")
city_connections["Boston Library"].append("Fenway Park")
city_connections["Quincy Market"].append("Fenway Park")
city_connections["Quincy Market"].append("Boston Library")


print(f"Bus routes in Boston after adding edges: {city_connections}")
