class Solution:
    def firstUniqChar(self, s: str) -> int:
        min_index = len(s)
        
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            first = s.find(c)
            
            if first != -1 and first == s.rfind(c):
                min_index = min(min_index, first)
                
        return min_index if min_index != len(s) else -1



       

        