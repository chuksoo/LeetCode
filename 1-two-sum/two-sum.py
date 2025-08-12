class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sums = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in two_sums:
                return [two_sums[diff], i]
            else:
                two_sums[val] = i
        
        return []

        