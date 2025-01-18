class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        idx = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[idx] = nums[i]
                idx += 1
        return len(seen)