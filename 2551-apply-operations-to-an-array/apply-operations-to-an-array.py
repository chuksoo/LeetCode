class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # modify the array according to the transformation rule
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # shift non-zero elements to the front
        ind = 0
        for num in nums:
            if num != 0:
                nums[ind] = num
                ind += 1

        # fill the remaining positions with zeros
        while ind < len(nums):
            nums[ind] = 0
            ind += 1
        return nums




        