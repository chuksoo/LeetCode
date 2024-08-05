class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return True
            while low < mid and nums[low] == nums[mid]:
                low += 1
                
            # the first half is ordered            
            if nums[low] <= nums[mid]:
                # target is in the first half
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
        
