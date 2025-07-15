class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargest(root, k):
    # implement this
    if not root:
        return
    right_nodes = countNodes(root.right) if root else 0

    if k == right_nodes + 1:
        return root.val
    elif k <= right_nodes:
        return kthLargest(root.right, k)
    else:
        return kthLargest(root.left, k - 1 - right_nodes)

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
print(kthLargest(root, 1))  # Expected output: 80
print(kthLargest(root, 5))  # Expected output: 55
print(kthLargest(root, 10))  # Expected output: 20
print(kthLargest(root, 3))  # Expected output: 65
print(kthLargest(root, 7))  # Expected output: 35
