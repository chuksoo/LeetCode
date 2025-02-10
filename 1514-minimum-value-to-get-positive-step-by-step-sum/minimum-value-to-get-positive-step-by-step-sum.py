class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        min_prefix_sum = min(nums)
        start_value = max(1, 1 - min_prefix_sum)
        return start_value

        