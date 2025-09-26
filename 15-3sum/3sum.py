class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # edge case
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        result = []

        for i in range(0, len(nums) - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # early termination
            if nums[i] > 0:
                break
            
            self.two_sums(nums, i, result)
        return result

    def two_sums(self, nums, idx, result):
        target = -nums[idx]
        left = idx + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[idx], nums[left], nums[right]])
                # handle duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1



        