class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return [lst for lst in arr1 if lst in arr2 and lst in arr3]
        