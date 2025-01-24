class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialize three pointers: start, current, end
        start, current, end = 0, 0, len(nums) - 1
        # iterate until current crosses the end pointer
        while current <= end:
            # if current element is 0, swap current with start element 
            if nums[current] == 0:
                nums[current], nums[start] = nums[start], nums[current]
                # increment current and start
                current += 1
                start += 1
            # if current element is 1, leave it in place and increment current
            elif nums[current] == 1:
                current += 1
            # if current element is 2, swap current with end
            else:
                nums[current], nums[end] = nums[end], nums[current]
                # decrement end
                end -= 1
        # return nums (which is sorted in place)
        return nums
