class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Time: O(NlogN), Space: O(N) - Not optimized
        # num_lst = [x for x in sorted(set(nums))]
        # num_lst = num_lst[::-1]
        # if len(num_lst) > 2:
        #     return num_lst[2] 
        # else:
        #     return num_lst[0]

        first = second = third = None
        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num
        return third if third is not None else first
        