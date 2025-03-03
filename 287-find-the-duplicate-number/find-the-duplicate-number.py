class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        duplicated_map = Counter(nums)
        for key in duplicated_map.keys():
            if duplicated_map[key] > 1:
                return key

        # for item in nums:
        #     if item in duplicated_map:
        #         duplicated_map[item] += 1
        #         return item
        #     else:
        #         duplicated_map[item] = 1
        
        