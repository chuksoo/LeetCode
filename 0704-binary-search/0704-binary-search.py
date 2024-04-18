class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # loop through each item in the array
        for i in range(len(nums)):
            # check if element at the current position matches the target
            if nums[i] == target:
                # if target found, return index
                return i
        # otherwise return -1
        return -1
    
            
        