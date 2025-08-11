from collections import deque  # Add this import

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    if not root:
        return True
    return isMirror(root.left, root.right)

def build_tree_from_list(values):
    """Helper to construct a binary tree from level-order list"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
input_tree_1 = [1,2,2,3,4,4,3]
input_tree_2 = [1,2,2,None,3,None,3]

root1 = build_tree_from_list(input_tree_1)
root2 = build_tree_from_list(input_tree_2)
print("Is the first tree symmetric?", isSymmetric(root1))
print("Is the second tree symmetric?", isSymmetric(root2))
