class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            count = sum(num <= mid for num in nums)

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low