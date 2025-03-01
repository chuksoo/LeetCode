class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Not efficient - Time: O(N log N), Space: O(N)
        nums.sort()
        distinct_avg = set()
        while nums:
            min_val = nums.pop(0)
            max_val = nums.pop(-1)
            distinct_avg.add((min_val + max_val) / 2)

        # Time: , Space:
        # from collections import deque
        # nums.sort()
        # nums = deque(nums)
        # distinct_avg = set()
        # while nums:
        #     min_val = nums.popleft()
        #     max_val = nums.pop()
        #     avgs = (min_val + max_val) / 2
        #     distinct_avg.add(avgs)
        return len(distinct_avg)
        