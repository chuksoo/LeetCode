class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # filter positive and negative numbers using list comprehension
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        
        # get the maximum count between positive and negative numbers
        return max(len(pos), len(neg))
        
        