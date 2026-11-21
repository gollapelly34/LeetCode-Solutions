class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        l = []
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                l.append(0)
                l.append(0)
            else:
                l.append(arr[i])
        for i in range(len(arr)):
            arr[i] = l[i]
        