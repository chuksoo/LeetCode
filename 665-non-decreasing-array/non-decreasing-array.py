class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False

                # Case 1: Modify nums[i] (decrease it)
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                # Case 2: Modify nums[i + 1] (increase it)
                else:
                    nums[i + 1] = nums[i]
        return True
        