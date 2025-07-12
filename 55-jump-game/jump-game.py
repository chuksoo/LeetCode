class Solution:
    def canJump(self, nums: List[int]) -> bool:


        max_jump_len = 0
        i = 0
        last_idx = len(nums) - 1
        # if nums[i] == 0 and last_idx == 1:
        #     return False

        while i <= max_jump_len and max_jump_len < last_idx:
            max_jump_len = max(max_jump_len, nums[i] + i)
            i += 1
        return max_jump_len >= last_idx

        