class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr = cur_min = 1
        for n in nums:
            temp = curr * n
            curr = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, curr)
        
        return res

        