class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0 and nums[right] == 1:
                left += 1
                right -= 1
            elif nums[left] == 1 and nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] == 0 and nums[right] == 0:
                left += 1
            else:
                right -= 1
        
        return nums
        