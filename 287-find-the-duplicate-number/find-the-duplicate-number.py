class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force - Time: O(N), Space: O(N)
        # from collections import Counter
        # duplicated_map = Counter(nums)
        # for key in duplicated_map.keys():
        #     if duplicated_map[key] > 1:
        #         return key

        # Two Pointer - Time: O(N), Space: 
        seen = set()
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == nums[right]:
                return nums[left]
            
            if nums[left] not in seen and nums[right] not in seen:
                seen.add(nums[left])
                seen.add(nums[right])
                left += 1
                right -= 1
            elif nums[left] in seen and nums[right] not in seen:
                seen.add(nums[right])
                right -= 1
                return nums[left]
            else:
                seen.add(nums[left])
                left += 1
                return nums[right]
            
        
        