class TreeNode:
    def __init__(self,data):
        self.val=data
        self.lelft=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,val):
        Node=TreeNode(val)
        if root is None:#treenode
            return Node
        #compare
        if val<root.val:
            root.left=self.insert(root.left,val)
        elif val>root.val:
            root.right=self.insert(root.right,val)
        return root