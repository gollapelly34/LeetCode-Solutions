class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        n = len(nums)
        s=0
        for i in range(n) :
            if(s<0):
                s=0
            s += nums[i]
            maxi = max(maxi,s)
        return maxi

