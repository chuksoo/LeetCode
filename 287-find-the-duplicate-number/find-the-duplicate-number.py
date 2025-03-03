class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicated_map = {}
        for item in nums:
            if item in duplicated_map:
                duplicated_map[item] += 1
                return item
            else:
                duplicated_map[item] = 1
        
        