class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time - O(nlogn) due to sorting, Space - O(1)
        # nums = sorted(nums)
        # range_x = [0, len(nums)]
        # if nums[-1] + 1 == len(nums):
        #     return len(nums)

        # for item in range(0, len(nums)):
        #     if item not in nums:
        #         return item

        # Time - O(1), Space - O(1)
        n = len(nums)
        expected_sum = n * (n + 1) / 2
        actual_sum = sum(nums)
        return int(expected_sum - actual_sum)


        
        