class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_lst = [x for x in sorted(set(nums))]
        num_lst = num_lst[::-1]
        if len(num_lst) > 2:
            return num_lst[2] 
        else:
            return num_lst[0]
        