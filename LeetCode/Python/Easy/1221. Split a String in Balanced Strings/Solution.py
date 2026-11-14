class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "L":
                count += 1
            elif s[i] == "R":
                count -= 1
            if count == 0:
                answer += 1
            
            




        return answer