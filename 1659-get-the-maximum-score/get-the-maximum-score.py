class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # initialize pointer
        i = j = 0
        # initialize sums
        sum1 = sum2 = 0
        # initialize result
        result = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else: 
                max_sums = max(sum1, sum2)
                max_sums += nums1[i]
                result += max_sums
                sum1 = sum2 = 0
                i += 1
                j += 1
        
        # handle remaining element in nums1 or nums2
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1

        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        # add final segment
        max_sums = max(sum1, sum2)
        result += max_sums

        return result % (10**9 + 7)        
        