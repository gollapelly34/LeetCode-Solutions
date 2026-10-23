class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz=[]
        z=[]
        for i in range(len(nums)):
            if nums[i]==0:
                z.append(nums[i])
            else:
                nz.append(nums[i])
        nz.extend(z)
        for i in range(len(nums)):
            nums[i] = nz[i]

   