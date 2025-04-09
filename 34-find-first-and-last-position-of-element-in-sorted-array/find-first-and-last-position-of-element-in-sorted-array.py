class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Optimal with Binary Search - Time: O(log n), SPace: O(1)
        start, end = 0, len(nums) - 1
        first = self.find_first(nums, target)
        if first == -1:
            return [-1, -1]

        last = self.find_last(nums, target)
        return [first, last]
        
        
    def find_first(self, nums, target):
        start, end = 0, len(nums) - 1
        first_ocurrence = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                first_ocurrence = mid
                end = mid -1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1
        return first_ocurrence

    def find_last(self, nums, target):
        start, end = 0, len(nums) - 1
        last_ocurrence = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                last_ocurrence = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1
        return last_ocurrence

    
        

        