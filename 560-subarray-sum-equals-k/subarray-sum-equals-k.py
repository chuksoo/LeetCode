class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize variables
        prefix_sum, count = 0, 0
        # store prefix sum frequencies
        hashmap = {0: 1}     
        # iterate thru nums       
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in hashmap:
                count += hashmap[prefix_sum - k]
            if prefix_sum in hashmap:
                hashmap[prefix_sum] += 1
            else:
                hashmap[prefix_sum] = 1
        return count




        