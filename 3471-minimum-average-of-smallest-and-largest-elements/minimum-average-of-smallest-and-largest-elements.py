class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Time: O(N log N), Space: O(N)
        # from collections import deque
        # avgs = []
        # nums.sort()
        # nums = deque(nums)
        # count, n = 0, len(nums)
        # while nums and count != n:
        #     min_elem = nums.popleft()
        #     max_elem = nums.pop()
        #     avgs.append((min_elem + max_elem) / 2)
        #     count += 1
        # return min(avgs)

        # Time: O(N log N), Space: O(1)
        nums.sort()
        left, right = 0, len(nums) - 1
        min_avg = float('inf')
        while left < right:
            min_avg = min(min_avg, ((nums[left] + nums[right])/ 2))
            left += 1
            right -= 1
        return min_avg


        