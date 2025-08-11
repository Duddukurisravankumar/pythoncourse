class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1
def pretree(root : TreeNode)->int:
    if root is not None:
        print(root.val)
        pretree(root.left)
        pretree(root.right)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left =TreeNode(7)
root.right.right =TreeNode(6)
root.right.left.left=TreeNode(7)
print(maxDepth(root))
pretree(root)

