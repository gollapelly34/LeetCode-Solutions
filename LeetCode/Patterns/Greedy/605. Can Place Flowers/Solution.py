class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i]= 0
                    n -= 1

                    if n==0:
                        return True

        




        return False



        
        