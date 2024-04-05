class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # set the value of first element in array
        num_i = nums[0]
        val = [num_i]
        for i in range(1, len(nums)):
            num_i += nums[i]
            val.append(num_i)
        return val
        