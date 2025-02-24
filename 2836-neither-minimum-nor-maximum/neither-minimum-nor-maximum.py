class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for num in nums:
            if num != min(nums) and num != max(nums):
                return num
        return -1
        