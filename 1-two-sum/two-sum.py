class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store complements
        complement_dict = {}
        # iterate thru array
        for i in range(len(nums)):
            # compute complement
            complement = target - nums[i]
            # check if complement exist in dictionary
            if complement in complement_dict:
                # if it does, return indices
                return [complement_dict[complement], i]
            # else, add current element and its index to dictionary
            complement_dict[nums[i]] = i

        # if no pair is found, return empty list
        return []

        
         