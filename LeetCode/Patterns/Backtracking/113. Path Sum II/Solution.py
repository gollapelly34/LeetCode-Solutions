# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root == None:
            return []
        if root.right == None and root.left == None :
            if targetSum == root.val :
                return [[root.val]]
            return []
        l = self.pathSum(root.left,targetSum-root.val)
        r = self.pathSum(root.right,targetSum - root.val)

        res = []

        for i in l:
            res.append([root.val] + i)
        for i in r:
            res.append([root.val]+ i)
        return res


        
        