class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = []
        ans = [-1]*len(nums1)
        
        for i in nums2:
            while s and i > s[-1]:
                x = s.pop()
                if x in nums1:
                    ans[nums1.index(x)] = i

            s.append(i)

        return ans

        