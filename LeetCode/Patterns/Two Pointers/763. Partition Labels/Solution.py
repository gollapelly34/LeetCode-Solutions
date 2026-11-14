class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        answer = []
        start = 0
        end = 0
        d = {}
        for i in range(len(s)):
            d[s[i]] = i

        for i in range(len(s)):
            end = max(end,d[s[i]])

            if i == end:     
                answer.append(end - start + 1)
                start = i + 1

        return answer

        