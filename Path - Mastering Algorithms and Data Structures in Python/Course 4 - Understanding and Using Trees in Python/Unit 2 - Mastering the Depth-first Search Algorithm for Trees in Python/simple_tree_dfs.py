class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_value):
        self.children.append(TreeNode(child_value))

    def depth_first_search(self):
        # Output traversal path for debugging
        print(self.value, end=' -> ')
        # Loop should initiate DFS on each child
        for child in self.children:
            child.depth_first_search()

# Construct a tree with a root node and its children
root_node = TreeNode('Root')
root_node.add_child('Left Child')
root_node.add_child('Right Child')

left_child_node = root_node.children[0]
left_child_node.add_child('Left Grandchild')
left_child_node.add_child('Right Grandchild')

# Perform a depth-first search traversal starting from the root node
print("DFS Traversal from Root Node:")
root_node.depth_first_search()
print("end")
