class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in s:
            if count < len(g) and i >= g[count]:
                count += 1
        return count
        
    
        