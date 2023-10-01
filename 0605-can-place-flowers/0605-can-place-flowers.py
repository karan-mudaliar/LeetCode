class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 0:
            return False
        
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n <=1) or n == 0:
                return True
            return False
        
        if len(flowerbed) == 2:
            if (n <= 1 and flowerbed[0] == 0 and flowerbed[1]== 0) or n == 0:
                return True
            return False

        if n == 0:
            return True

        sliding = [0,0,0]

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n == 0:
                return True
            
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1 
            if n == 0:
                return True
                
        for i in range(1,len(flowerbed)-2):
            if n == 0:
                return True
            if flowerbed[i:i+3] == sliding:
                flowerbed[i+1] = 1
                n -= 1
                
        

        return n == 0