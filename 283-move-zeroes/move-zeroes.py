class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left pointer for writing non-zero elements
        left = 0
        # right pointer for scanning array
        for right in range(len(nums)):
            # if right is non-zero, swap and increase left pointer
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        # return nums
        return nums
        