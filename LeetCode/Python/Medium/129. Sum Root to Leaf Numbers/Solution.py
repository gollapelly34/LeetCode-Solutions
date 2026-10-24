# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def solve(root,num):
            if root == None:
                return 0
            num = num * 10 + root.val
            if(root.left  == None and root.right == None):
                return num

            l = solve(root.left,num)
            r = solve(root.right,num)
            return l+r

        return solve(root,0)
        
        