class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + ((right - left) // 2)
            # compare distance from x of arr[mid] vs arr[mid+k]
            if x - arr[mid] > arr[mid + k] - x:
                # window starting at mid is too far left, shift right
                left = mid + 1
            else:
                # window at mid is as good or better, keep it in play
                right = mid 
        # left == right is now the optimal window start
        return arr[left : left + k]

