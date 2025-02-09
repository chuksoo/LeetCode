class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # initialize pointers for sliding window
        left = 0
        max_length = 0
        zero_count = 0

        # iterate over array with right pointer
        for right in range(len(nums)):
            # if current element is 0, increment zero count
            if nums[right] == 0:
                zero_count += 1

            # if number of zeros exceed k, shrink window from left
            while zero_count > k:
                # if element at left pointer is 0, decrement the zero count
                if nums[left] == 0:
                    zero_count -= 1
                # move left pointer to right
                left += 1
            # calculate max length of window
            max_length = max(max_length, right - left + 1)
            
        return max_length
        

        