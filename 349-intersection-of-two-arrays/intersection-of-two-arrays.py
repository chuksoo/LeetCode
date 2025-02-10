class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [lst for lst in set(nums1) if lst in set(nums2)]
        