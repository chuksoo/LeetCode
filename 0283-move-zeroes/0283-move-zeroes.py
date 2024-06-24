class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize two pointers
        write = 0
        read = 0
        # Move non-zero element to the front
        while read < len(nums):
            if nums[read] != 0:
                # Swap elements at write and read positions
                nums[write] = nums[read]
                write += 1
            read += 1

        # Fill the rest with zeroes
        while write < len(nums):
            nums[write] = 0
            write += 1
        return nums

        