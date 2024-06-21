class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
        
# Alternative approach using Two Pointer
#         sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        
#         low = 0
#         high = len(sorted_nums) - 1
#         while low < high:
#             twins = sorted_nums[low][0] + sorted_nums[high][0]
#             if twins == target:
#                 return [sorted_nums[low][1], sorted_nums[high][1]]
#             elif twins < target:
#                 low += 1
#             else:
#                 high -= 1        
#         return []
        
            
        
      