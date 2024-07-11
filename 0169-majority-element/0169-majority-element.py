class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        max_k, max_v = 0, 0
        for k, v in freq.items():
            if v > max_v:
                max_v = v
                max_k = k
        return max_k
        