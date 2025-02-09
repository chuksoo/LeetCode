class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # slide window across array
        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k