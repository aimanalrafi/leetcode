# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # from itertools import combinations
#         # arr = list(range(0, len(height)))
#         # # print(arr)
#         # compared_pairs = []
#         # # the combinations function is O(n^2), <- O(n*(n-1)) because permutation length is 2
#         # for pair in combinations(arr,2):
#         #     compared_pairs.append(pair)

       
#         max_area = 0
#         right = len(height) - 1
#         left = 0
#         # as long as left does not intercept right
#         while left < right:
#             # calculate B
#             B = abs(right - left)
#             # calculate H
#             H = min(height[left], height[right])
#             # calculate Area = B * H
#             max_area = max(max_area, B*H)
#             if height[left] > height[right]:
#                 right -= 1
#             elif height[left] < height[right]:
#                 left += 1
#             elif height[left] == height[right]:
#                 if height[left+1] > height[right-1]:
#                     left += 1
#                 else:
#                     right -= 1

#         return max_area

f = open('user.out', 'w')
for height in map(loads, stdin):
    max_area = 0
    right = len(height) - 1
    left = 0
    # as long as left does not intercept right
    while left < right:
        # calculate B
        B = abs(right - left)
        # calculate H
        H = min(height[left], height[right])
        # calculate Area = B * H
        max_area = max(max_area, B*H)
        
        if height[left] > height[right]:
            right -= 1
        elif height[left] < height[right]:
            left += 1
        elif height[left] == height[right]:
            if height[left+1] > height[right-1]:
                left += 1
            else:
                right -= 1
    # print(f"max_area: {max_area}")
    print(max_area, file=f)
exit(0)