class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        c = 0
        s = 0
        for i in range(k):
            s += arr[i]
        if s / k >= threshold:
            c+= 1
        for i in range(k,len(arr)):
            s =  s + arr[i] - arr[i-k]

            if s/k>= threshold:
                c += 1
        return c
        
    