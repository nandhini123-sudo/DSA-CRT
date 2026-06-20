class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
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
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.val)
            self.Inorder(root.right)
bst=BST()
root=None
for i in [50,30,20,70,80]:
    root=bst.insert(root,i)
bst.Inorder(root)