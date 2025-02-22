class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_val = -inf
        for i, val in enumerate(nums):
            if val > max_val:
                max_val = val
                index = i
        return index

        