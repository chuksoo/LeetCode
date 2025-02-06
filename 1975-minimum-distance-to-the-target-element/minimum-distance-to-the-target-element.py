class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums == []:
            return 0

        min_val = 9999
        for i, val in enumerate(nums):
            if nums[i] != target:
                i += 1
            elif nums[i] == target:
                get_val = abs(i - start)
                if get_val < min_val:
                    min_val = get_val
                i += 1
        return min_val

        
        

        