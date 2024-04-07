class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_lst = []
        for x in arr:
            new_lst.append(x)
            if x == 0:
                new_lst.append(x)
        for i in range(len(arr)):
            arr[i] = new_lst[i]
                
        