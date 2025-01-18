class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        my_dict = Counter(nums)
        for value in my_dict.values():
            if value >= 2:
                return True
        return False
