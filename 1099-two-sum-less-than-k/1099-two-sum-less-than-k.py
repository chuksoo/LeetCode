class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            sum_k = nums[left] + nums[right]
            if sum_k < k:
                answer = max(sum_k, answer)
                left += 1
            else:
                right -= 1
        return answer
        