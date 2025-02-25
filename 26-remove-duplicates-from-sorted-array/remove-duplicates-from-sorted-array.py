class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(N), Space: O(N)
        # seen = set()
        # idx = 0
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #         nums[idx] = nums[i]
        #         idx += 1
        # return len(seen)

        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1 