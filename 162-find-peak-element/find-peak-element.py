class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # Time - O(N), Space - O(1)
        # max_val = -inf
        # for i, val in enumerate(nums):
        #     if val > max_val:
        #         max_val = val
        #         index = i
        # return index

        # Time - O(Nlog N), Space - O(1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid 
            else:
                left = mid + 1
        return left
                

        