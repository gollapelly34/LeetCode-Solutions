# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        if root == None:
            return None
        def findSum(node, s):
            if node == None:
                return 0

            s = s * 2 + node.val

            if node.left == None and node.right == None:
                return s

            return findSum(node.left, s) + findSum(node.right, s)

        return findSum(root, 0)
        