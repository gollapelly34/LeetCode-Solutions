class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(ransomNote)
        c = Counter(magazine)
        
        for i in d:
            if i not in c or d[i]>c[i]:
                return False
        return True
        
        