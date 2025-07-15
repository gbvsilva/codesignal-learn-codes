class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return f'Node({self.val})'

def insert_BST(root, node):
    # TODO: Insert a node into the BST
    if root is None:
        return node
    if root.val < node.val:
        root.right = insert_BST(root.right, node)
    else:
        root.left = insert_BST(root.left, node)
    return root

def search_BST(root, value):
    # TODO: Perform the search for value in the BST
    if root is None:
       return
    if root.val < value:
        return search_BST(root.right, value)
    elif root.val > value:
        return search_BST(root.left, value)
    return root

r = Node(50)
insert_BST(r, Node(20))
insert_BST(r, Node(70))
insert_BST(r, Node(10))
insert_BST(r, Node(30))
insert_BST(r, Node(60))
insert_BST(r, Node(80))

print(search_BST(r, 70)) # returns Node(70)
print(search_BST(r, 30)) # returns Node(30)
print(search_BST(r, 80)) # returns Node(80)
print(search_BST(r, 40)) # returns None
print(search_BST(r, 50)) # returns Node(50)
print(search_BST(r, 90)) # returns None
