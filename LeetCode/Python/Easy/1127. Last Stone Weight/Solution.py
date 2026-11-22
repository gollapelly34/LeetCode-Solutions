class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        l = []
        for i in range(len(stones)):
            l.append(-stones[i])
        heapq.heapify(l)

        while(len(l) > 1):
            first = heapq.heappop(l)
            second = heapq.heappop(l)
            if (first != second):
                heapq.heappush(l,first-second)
        return -l[0] if l else 0
        


    
        