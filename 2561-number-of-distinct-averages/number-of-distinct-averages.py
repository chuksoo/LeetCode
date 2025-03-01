class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        distinct_avg = set()
        while nums:
            min_val = nums.pop(0)
            max_val = nums.pop(-1)
            avgs = (min_val + max_val) / 2
            distinct_avg.add(avgs)
        return len(distinct_avg)
        