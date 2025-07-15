class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_height_diff(root):
    max_diff = [0]
    def height(node):
        # implement this
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        max_diff[0] = max(max_diff[0], abs(left - right))
        return 1 + max(left, right)

    if root is None:
        # implement this
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    # implement this
    return max(max_diff[0], abs(left_height - right_height))

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1
