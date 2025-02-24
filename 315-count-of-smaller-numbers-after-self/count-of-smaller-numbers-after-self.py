class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Not optimal
        # result = []
        # fast = 0
        # while fast < len(nums):
        #     count = 0
        #     for i in range(fast, len(nums)):
        #         if nums[fast] > nums[i]:
        #             count += 1
        #     result.append(count)
        #     fast += 1
        # return result

        # Time: O(nlog n)
        from sortedcontainers import SortedList
        sorted_list = SortedList()
        result = []
        for num in reversed(nums):
            index = sorted_list.bisect_left(num)
            result.append(index)
            sorted_list.add(num)
        return result[::-1]
        