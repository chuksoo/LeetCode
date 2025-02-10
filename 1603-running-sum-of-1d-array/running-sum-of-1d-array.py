class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # One Pass - Time: O(N), Space: O(N)
        # prefix = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix.append(nums[i] + prefix[-1])
        # return prefix

        # One Pass, In-Place - Time: O(N), Space - O(1)
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

        