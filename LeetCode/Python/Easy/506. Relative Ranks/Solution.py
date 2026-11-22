class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort_scores = sorted(score,reverse=True)
        rank = {}
        for i, value in enumerate (sort_scores):
            if i == 0:
                rank[value] = "Gold Medal"
            elif i== 1:
                rank[value] = "Silver Medal"
            elif i ==2:
                rank[value] = "Bronze Medal"
            else:
                rank[value] = str(i+1)
        result = []
        for x in score:
            result.append(rank[x])

        return result

        