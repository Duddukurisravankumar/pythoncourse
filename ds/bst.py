class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.left, lower, val):
            return False
        if not helper(node.right, val, upper):
            return False
        return True
    return helper(root)
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)
def validate_and_print(root):
    if isValidBST(root):
        print("BST is valid. Inorder traversal:")
        print_inorder(root)
        print() 
    else:
        return False
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(7, None, TreeNode(8))
result = validate_and_print(root)
if result == False:
    print(result)
