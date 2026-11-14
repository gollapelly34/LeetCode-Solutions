class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            perimeter = a+b+c
            if b+c > a:
                return perimeter
            else:
                return 0