class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        min_val = nums[left]
        while left < len(nums):
            if nums[left] <= min_val:
                min_val = nums[left]
                left += 1
            else:
                left += 1
        return min_val


        