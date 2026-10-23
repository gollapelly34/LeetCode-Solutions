class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = 0
        n = len(nums)
        for i in range(k):
            s += nums[i]

        maxi = s
        for i in range(k,n):
            s = s + nums[i] - nums[i-k]
            maxi = max(maxi,s)
        return maxi/k
            
