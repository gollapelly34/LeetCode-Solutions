# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
         def check(root,l):
            if(root==None):
                return 0
            l.append(root.val)
            temp=0
            count=0
            for i in reversed(l):
                temp+=i
                if(temp==targetSum):
                    count+=1
            count+=check(root.left,l)
            count+=check(root.right,l)
            l.pop()
            return count
        return check(root,[])



        """
        if root == None:
            return 0

        def countPath(node,target):
            if node == None:
                return 0

            c = 0
            if node.val == target:
                c += 1
            c += countPath(node.left, target - node.val)
            c += countPath(node.right, target - node.val)

            return c

        return (countPath(root, targetSum)+ self.pathSum(root.left, targetSum)+ self.pathSum(root.right, targetSum))
        """
        