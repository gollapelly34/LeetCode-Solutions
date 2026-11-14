class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        i,j = 0,0
        while( i<len(g) and j<len(s)):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count





        """
        g.sort()
        s.sort()
        count = 0
        for i in s:
            if count < len(g) and i >= g[count]:
                count += 1
        return count
        """

        
    
        