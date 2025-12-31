class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3) 
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)
   
def print_tree_preorder(node):
    if node is not None:
        print(node.val)
        print_tree_preorder(node.left)
        print_tree_preorder(node.right)
print("Binary Tree Structure: ")
print_tree_preorder(root)
