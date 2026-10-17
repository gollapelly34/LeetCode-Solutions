# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def inorder(self,root,l):
        if root == None:
            return l
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root == None:
            return None
        l = []
        self.inorder(root,l)
        return l[k-1]

        """
        l = []

        def inorder(root):
            if root == None:
                return 

            inorder(root.left)
            l.append(root.val)
            inorder(root.right)

        inorder(root)
        return l[k-1]
        """
