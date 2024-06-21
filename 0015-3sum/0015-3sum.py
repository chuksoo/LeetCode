class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    triplet = nums[i] + nums[low] + nums[high]
                    if triplet < 0:
                        low += 1
                    elif triplet > 0:
                        high -= 1
                    else:
                        res.append([nums[i], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
        return res
                        
        
        