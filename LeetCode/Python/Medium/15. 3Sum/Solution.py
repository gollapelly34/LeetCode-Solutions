class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            j = i + 1
            while j < n:
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]

                        if triplet not in ans:
                            ans.append(triplet)

                j += 1
        return ans