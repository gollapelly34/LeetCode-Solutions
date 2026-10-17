# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root == None:
            return None
        temp = root
        if(key<temp.val):
            temp.left = self.deleteNode(root.left, key)
        elif(key>temp.val):
            temp.right = self.deleteNode(root.right, key)
        else:
            #No children 
            if(temp.left == None and temp.right == None):
                return None
             #one child
            elif (temp.left == None and temp.right != None):
                return temp.left
            elif(temp.left == None and temp.right != None):
                return temp.right
            else:
                # 2 children
                temp2 = temp.right
                while(temp2.left):
                    temp2 = temp2.left
                temp.val = temp2.val
                temp.right = self.deleteNode(temp.right,temp2.val)
        return root 










"""
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if root.left == None:
                return root.right

            if root.right == None:
                return root.left

            temp = root.right

            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root
        """
