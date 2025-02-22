class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        good_pairs = 0
        for num in nums:
            if num in freq_map:
                good_pairs += freq_map[num]
            freq_map[num] += 1
        return good_pairs

        