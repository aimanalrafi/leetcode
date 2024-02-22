class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # optimize: at least two 0s for each flower to plant
        if n > len(flowerbed):
            # print("n > len(flowerbed)")
            return False
        elif n == 0:
            # print("n == 0")
            return True
        # elif (len(flowerbed) > 1) and (flowerbed.count(0) < 2*n):
        #     print(f"optimized because of 2n condition")
        #     return False
        elif (len(flowerbed) == 1) and (flowerbed[0] == 1):
            # print(f"[1]")
            return False
        elif (len(flowerbed) == 1) and (flowerbed[0] == 0):
            return True
        # print(f"length of flowerbed = {len(flowerbed)}")
        i = 0
        flowerPlanted = False
        while i < len(flowerbed):
            flowerPlanted = False
        
            if (i == 0) and (flowerbed[i+1] == 0) and (flowerbed[i] == 0):
                # print(f"plant flower at {i}")
                flowerbed[i] = 1
                n -= 1
                flowerPlanted = True
            elif (i == len(flowerbed) - 1) and (flowerbed[i-1] == 0) and (flowerbed[i] == 0):
                # print(f"plant flower at {i}")
                flowerbed[i] = 1
                n -= 1
                flowerPlanted = True
            elif (flowerbed[i] == 0) and (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                # print(f"plant flower at {i}")
                flowerbed[i] = 1
                n -= 1
                flowerPlanted = True
            elif (flowerbed[i] == 0) and (i == len(flowerbed) - 2) and (flowerbed[i + 1] == 0):
                # print(f"plant flower at {i}")
                flowerbed[i] = 1
                n -= 1
                flowerPlanted = True
            

            if n == 0:
                # print(f"n = 0; flowerbed {flowerbed}")
                return True
            
            if flowerPlanted == True:
                i += 2
            else:
                i += 1
        return False

            