class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using list comprehension - Time: O(N), Space: O(N)
        # return [lst for lst in set(nums1) if lst in set(nums2)]

        # Using Two pointer approach - Time: O(N), Space: O(1)
        nums1.sort()
        nums2.sort()

        i = j = 0
        intersect = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else: 
                j += 1
        results = [result for result in intersect]
        return results
        