class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        k = n - 1
        while k >= 0:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result[k] = left_square
                left += 1
            else:
                result[k] = right_square
                right -= 1
            k -= 1
        return result
    