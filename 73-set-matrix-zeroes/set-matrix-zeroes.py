class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zero = False
        col_zero = False

        for row in range(m):
            if matrix[row][0] == 0:
                col_zero = True
        for col in range(n):
            if matrix[0][col] == 0:
                row_zero = True
        
        # use fist row and fist columns as marker
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        # set matrix elements to zero based on markers
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        # handle irst row and fist column separately
        if col_zero:
            for row in range(m):
                matrix[row][0] = 0
        if row_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        return matrix
        

        