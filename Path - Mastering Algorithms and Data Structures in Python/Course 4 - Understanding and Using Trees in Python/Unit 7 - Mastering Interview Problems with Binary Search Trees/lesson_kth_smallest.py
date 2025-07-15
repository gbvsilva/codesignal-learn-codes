class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    # The number of nodes in the left subtree of the root
    left_nodes = countNodes(root.left) if root else 0

    # If k is equal to the number of nodes in the left subtree plus 1,
    # That means we must return the root's value as we've reached the k-th smallest
    if k == left_nodes + 1:
        return root.val
    # If there are more than k nodes in the left subtree,
    # The k-th smallest must be in the left subtree.
    elif k <= left_nodes:
        return kthSmallest(root.left, k)
    # If there are less than k nodes in the left subtree,
    # The k-th smallest must be in the right subtree.
    else:
        return kthSmallest(root.right, k - 1 - left_nodes)

def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

# Creating the BST
root = Node(50)
root.left = Node(20)
root.right = Node(60)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(55)
root.right.right = Node(70)
root.left.right.left = Node(25)
root.left.right.right = Node(35)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

# Now, let's test the function with the new binary tree
print(kthSmallest(root, 1)) # Expected output: 10
print(kthSmallest(root, 5)) # Expected output: 35
print(kthSmallest(root, 10)) # Expected output: 70
print(kthSmallest(root, 3)) # Expected output: 25
print(kthSmallest(root, 7)) # Expected output: 55
