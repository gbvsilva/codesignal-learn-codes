class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def bst_insert(root, node):
    if root is None:
        root = node
    elif root.val < node.val:
        root.right = bst_insert(root.right, node)
    else:
        root.left = bst_insert(root.left, node)
    return root

def bst_traversal_inorder(root):
    if root:
        bst_traversal_inorder(root.left)
        print(root.val)
        bst_traversal_inorder(root.right)

r = TreeNode(50)
bst_insert(r, TreeNode(30))
bst_insert(r, TreeNode(20))
bst_insert(r, TreeNode(40))
bst_insert(r, TreeNode(70))
bst_insert(r, TreeNode(60))
bst_insert(r, TreeNode(80))

bst_traversal_inorder(r)
