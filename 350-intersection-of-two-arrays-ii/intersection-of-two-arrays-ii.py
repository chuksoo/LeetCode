class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        from collections import Counter
        freq_map = Counter(nums1)

        result = []
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                result.append(num)
                freq_map[num] -= 1
        return result


