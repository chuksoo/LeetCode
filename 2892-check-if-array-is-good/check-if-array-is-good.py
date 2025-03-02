class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = max(nums)
        if len(nums) != n + 1:
            return False

        from collections import Counter
        freq_map = Counter(nums)

        for i in range(1, n-1):
            if freq_map[i] != 1:
                return False

        if freq_map[n] != 2:
            return False

        return True
        