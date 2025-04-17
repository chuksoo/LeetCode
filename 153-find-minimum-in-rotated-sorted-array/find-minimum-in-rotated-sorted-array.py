class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # Time - O(N), Space - O(1)
        # left = 0
        # min_val = nums[left]
        # while left < len(nums):
        #     if nums[left] <= min_val:
        #         min_val = nums[left]
        #         left += 1
        #     else:
        #         left += 1
        # return min_val

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


        