class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse = True)
        answer = 0
        for a,b in boxTypes:
            if a <= truckSize:
                answer = answer + (a*b)
                truckSize -= a
            else:
                answer += truckSize * b
                truckSize = 0
        return answer

        


        