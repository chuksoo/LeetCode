class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_set = set()
        hash_lst = []
        for i in range(0, len(nums)):
            if nums[i] in hash_set:
                hash_lst.append(nums[i])
            hash_set.add(nums[i])   
        return hash_lst
            
                
            
        