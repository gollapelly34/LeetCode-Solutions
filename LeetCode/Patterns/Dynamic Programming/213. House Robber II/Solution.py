class Solution:
    def solve(self,nums,s,e):
        n = len(nums)
        dp = [0] * len(nums)
        dp[s] = nums[s]
        if s+1 <= e:
            dp[s+1] = max(nums[s],nums[s+1])
        for i in range(s+2,e+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[e]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        case1 = self.solve(nums,0,n-2)
        case2 = self.solve(nums,1,n-1)
        return max(case1,case2)

        

    