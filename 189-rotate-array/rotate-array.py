class Solution:
    def reverse_items(self, l: List[int], start: int, end: int) -> None:
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1
        
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse_items(nums, 0, n - 1)
        self.reverse_items(nums, 0, k - 1)
        self.reverse_items(nums, k, n - 1)
        
        