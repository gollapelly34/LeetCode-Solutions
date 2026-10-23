class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        for i in range(k):
            if (s [i] in "aeiou"):
                c += 1
        maxi = c
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                c += 1
            if s[i-k] in "aeiou":
                c -= 1
            maxi = max(maxi,c)
        return maxi