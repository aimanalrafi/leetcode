class Solution:
    # count = 0
    def maxOperations(self, nums: List[int], k: int) -> int:

        c_nums = Counter(nums)
        count = 0
        for x in c_nums:
            y = k - x
            if y == x:
                count += floor(c_nums[x]/2)
            elif (x + y == k) and x < y:
                count += min(c_nums[x], c_nums[y])

        return count

        # nums.sort()

        # count = 0
        # left = 0
        # right = len(nums) - 1

        


        # while left < right:
        #     if (nums[left] + nums[right]) == k:
        #         count += 1
        #         left += 1
        #         right -= 1
        #     elif (nums[left] + nums[right]) < k:
        #         left += 1
        #     else:
        #         right -= 1
            
        # return count

        

                
