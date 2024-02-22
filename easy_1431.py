class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # res_array = [True for _ in range(len(candies))]
        res_array = []
        x = 0
        while x < len(candies):
            if (candies[x] + extraCandies) >= max(candies):
                res_array.append(True)
            else:
                res_array.append(False)
            # candies[x] += extraCandies
            # if max(candies) != candies[x]:
            #     res_array[x] = False
            # candies[x] -= extraCandies
            # print(f"iteration {x}: max={max(candies)}, current_candy={candies[x]}")
            x += 1

        return res_array
                 