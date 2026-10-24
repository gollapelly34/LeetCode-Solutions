# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
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

        return (countPath(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))
        
        