class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for k, v in dict.items():
            if v >= 2:
                return k
        