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
        def findSum(node, num):
            if node == None:
                return 0

            num = num * 2 + node.val

            if node.left == None and node.right == None:
                return num

            return findSum(node.left, num) + findSum(node.right, num)

        return findSum(root, 0)
        