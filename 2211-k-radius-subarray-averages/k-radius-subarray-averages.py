class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # initialization
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        result = [-1] * n

        # compute prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # compute k-radius averages
        for i in range(k, n - k):
            left_index = i - k
            right_index = i + k
            window_sum = prefix_sum[right_index + 1] - prefix_sum[left_index]
            result[i] = window_sum // (2 * k + 1)
        return result
        