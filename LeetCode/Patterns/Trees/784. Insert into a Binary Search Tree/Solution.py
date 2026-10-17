# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        new_node = TreeNode(val)
        if root == None:
            return new_node
        temp = root
        while(True):
            if(val<temp.val):
                if(temp.left==None):
                    temp.left = new_node
                    break
                else:
                    temp=temp.left
            elif(val>temp.val):
                if(temp.right == None):
                    temp.right = new_node
                    break
                else:
                    temp = temp.right
        return root 










        """
        if root == None:
            return TreeNode(val)
        temp = root
        while temp:
            if val > temp.val:
                if temp.right == None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
            else:
                if temp.left == None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
        return root
        """
