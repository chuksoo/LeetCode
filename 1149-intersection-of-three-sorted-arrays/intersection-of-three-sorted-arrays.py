class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Using list comprehension - Time: O(N), Space: O(N)
        # return [lst for lst in arr1 if lst in arr2 and lst in arr3]
        
        # Using three pointers
        i, j, k = 0, 0, 0
        result = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr2[j] < arr3[k]:
                    j += 1
                else:
                    k += 1
        return result
