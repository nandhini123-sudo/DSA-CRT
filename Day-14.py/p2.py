class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
            return res
        return inorder(root, [])

# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

obj = Solution()
print(obj.inorderTraversal(root))