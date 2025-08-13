class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        range_x = [0, len(nums)]
        if nums[-1] + 1 == len(nums):
            return len(nums)

        for item in range(0, len(nums)):
            if item not in nums:
                return item

        
        