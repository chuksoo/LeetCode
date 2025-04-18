class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time - O(M+N), Space - O(1)
        k = 0
        fast = slow = 0
        while fast <= len(nums1) - 1 and slow <= len(nums2) - 1:
            if nums1[fast] != 0:
                fast += 1
            elif nums1[fast] == 0:
                nums1[fast] = nums2[slow]
                fast += 1
                slow += 1
        return nums1.sort()



        