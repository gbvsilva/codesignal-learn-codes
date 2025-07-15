class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

# Define the tree
tree_root = TreeNode('Apple')
root_left = TreeNode('Banana')
root_right = TreeNode('Cherry')
tree_root.add_child(root_left)
tree_root.add_child(root_right)

root_left.add_child(TreeNode('Date'))
root_left.add_child(TreeNode('Elderberry'))

root_right.add_child(TreeNode('Pear'))
root_right.children[0].add_child(TreeNode('Plum'))
root_right.add_child(TreeNode('Grape'))

# TODO: Add a plum under pear

def print_tree(node):
    # TODO: print the whole tree, first printing the root, and then all its children recursively
    if not node:
        return
    print(f'Fruit -> {node.value}')
    for child in node.children:
        print_tree(child)

print_tree(tree_root)
