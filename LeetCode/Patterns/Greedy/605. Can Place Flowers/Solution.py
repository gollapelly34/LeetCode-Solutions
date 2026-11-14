class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    
    
        for i in range(len(flowerbed)):
            left = False
            right = False
            if flowerbed[i] == 0:
                #left
                if i == 0 or [i - 1] == 0:
                    left = True
                    #right

                if i == n - 1 or flowerbed[i + 1] == 0:
                    right = True


                if left and right:
                    flowerbed[i]= 0
                    n -= 1

                if n==0:
                    return True

        




        return False



        
        