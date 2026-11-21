class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in s:
            if d[i] == 1:
                return s.index(i)
        return -1





        """
        min_index = len(s)
        
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            first = s.find(c)
            
            if first != -1 and first == s.rfind(c):
                min_index = min(min_index, first)
                
        return min_index if min_index != len(s) else -1


"""
       

        