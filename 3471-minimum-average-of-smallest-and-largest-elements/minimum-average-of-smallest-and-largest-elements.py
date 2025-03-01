class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        from collections import deque
        avgs = []
        nums.sort()
        nums = deque(nums)
        count, n = 0, len(nums)
        while nums and count != n:
            min_elem = nums.popleft()
            max_elem = nums.pop()
            avgs.append((min_elem + max_elem) / 2)
            count += 1
        return min(avgs)

        