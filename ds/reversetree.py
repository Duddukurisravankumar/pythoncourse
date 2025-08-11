from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
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
def tree_to_list(root):
    """Convert tree to level-order list"""
    if not root:
        return []
    output = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            output.append(None)
    while output and output[-1] is None:
        output.pop()
    return output
input_tree = [4,2,7,1,3,6,9]
root = build_tree_from_list(input_tree)
inverted_root = invertTree(root)
output_list = tree_to_list(inverted_root)
print("Output:", output_list)
