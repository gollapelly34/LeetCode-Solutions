# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []
        q = deque([root])
        res = []

        while q:
            level = []
            n = len(q)

            for i in range(n):
                temp = q.popleft()
                level.append(temp.val)

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

            res.append(level)

        return res
