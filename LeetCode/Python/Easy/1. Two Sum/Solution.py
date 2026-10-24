class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d:
                return [d[x],i]
            d[nums[i]] = i
        """





        