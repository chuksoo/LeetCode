class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        # create dictianry of items in list
        nums_map = Counter(nums)
        # get max of value in dictionary
        max_val = max(nums_map.values())
        result = [[] for _ in range(max_val)]

        # iterate thru item and value count
        for item, count in nums_map.items():
            # for i in range of count
            for i in range(count):
                # append item to result i
                result[i].append(item)
        # return result
        return result
        