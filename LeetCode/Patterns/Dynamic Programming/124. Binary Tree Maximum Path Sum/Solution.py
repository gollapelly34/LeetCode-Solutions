# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = [root.val]

        def solve(root):
            if root == None:
                return 0

       
            l =  max(0,solve(root.left))
            r = max(0,solve(root.right))
            maxi[0] = max(maxi[0], l + r + root.val)
            return root.val + min(l,r)
        solve(root)
        return maxi[0] 



