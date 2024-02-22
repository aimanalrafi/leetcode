class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # only works if copy can be created
        # initial_len = len(nums)
        # nums = [num for num in nums if num != 0]
        # nums += [0] * (initial_len - len(nums))
        
        j = 0
        placeholder = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                placeholder = nums[j]
                nums[j] = nums[i]
                nums[i] = placeholder
                j += 1
