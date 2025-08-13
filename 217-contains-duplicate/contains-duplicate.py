class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time - O(N), Space - O(1)
        # my_set = set()
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     my_set.add(num)
        # return False

        return len(set(nums)) != len(nums)
