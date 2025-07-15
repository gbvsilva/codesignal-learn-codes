# TODO: Define your Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# TODO: Define a binary tree using your Node class
binary_tree_root = Node(1)
binary_tree_root.left = Node(2)
binary_tree_root.right = Node(3)
binary_tree_root.right.left = Node(4)
binary_tree_root.right.right = Node(5)

# TODO: Implement a function to perform in-order traversal
def in_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    print(f'Node -> {node.value}')
    in_order_traversal(node.right)

# TODO: Print the nodes of the binary tree using the in-order traversal method
in_order_traversal(binary_tree_root)
