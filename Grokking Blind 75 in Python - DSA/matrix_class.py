class Matrix:
    rows = 0
    columns = 0
    matrix = []
    matrixRow = []
    dataCount = 0
    matrixList = []
    tempProduct = 0
    
    def __init__(self, Rows, Columns, Data = []):
        if Data == []:
            Data = [None] * (Rows * Columns)
        self.matrix = []
        self.rows = Rows
        self.columns = Columns
        for i in range(Rows):
            self.matrixRow = []
            for j in range(Columns):
                self.matrixRow.append(
                    Data[self.dataCount])
                self.dataCount += 1
            self.matrix.append(self.matrixRow)
            
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __add__(self, Value):
        self.matrixList = []
        if type(Value) == list:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrixList.append(
                        self.matrix[i][j] + Value[i][j])
            
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrixList.append(
                        self.matrix[i][j] + Value)
                    
        return Matrix(self.rows, self.columns, 
                      self.matrixList)
    
    def __mul__(self, MatrixIn):
        self.matrixList = []
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrixList.append(
                    self.matrix[i][j] * MatrixIn[i][j])
        return Matrix(self.rows, self.columns, 
                      self.matrixList)
        
    def dot(self, MatrixIn):
        self.matrixList = []
        for i in range(self.rows):
            for j in range(MatrixIn.columns):
                tempProduct = 0
                for k in range(self.columns):
                    tempProduct += self.matrix[i][k] * \
                        MatrixIn[k][j]
                self.matrixList.append(tempProduct)
        return Matrix(self.rows, MatrixIn.columns, self.matrixList)
    
    def transpose(self):
        self.matrixList = []
        for i in range(self.columns):
            for j in range(self.rows):
                self.matrixList.append(self.matrix[j][i])
        return Matrix(self.columns, self.rows, self.matrixList)
    
    def copyMatrix(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrixList.append(self.matrix[i][j])
        return Matrix(self.rows, self.columns, self.matrixList)
    
    def determinant(self, Result=0):
        # Address the simplest case first, the 2 X 2 matrix.
        if len(self.matrix) == 2:
            twoOut = self.matrix[0][0] * self.matrix[1][1] - \
                self.matrix[1][0] * self.matrix[0][1]
            return twoOut
        
        # Determine the number of rows in a matrix larger
        # than 2 X 2.
        rows = list(range(len(self.matrix)))
        
        # Process each focus column in turn.
        for focus in rows:
        
            # Create a copy of the matrix.
            submatrix = self.copyMatrix()

            # Remove the first row of the submatrix.
            submatrix.matrix = submatrix.matrix[1:]

            # Obtain the number of remamining rows to
            # process.
            subrows = len(submatrix.matrix)

            # Create the next smaller size matrix by slicing
            # out the focus rows.
            for i in range(subrows):
                submatrix.matrix[i] = \
                    submatrix.matrix[i][0:focus] + \
                    submatrix.matrix[i][focus+1:]
            
            # Determine the sign to use when performing the
            # multiplication.
            sign = (-1) ** (focus % 2)
            
            # Call the determinant() function recursively
            # with each smaller matrix.
            subdeterminant = submatrix.determinant()
            
            # Total the returns from the recursive calls.
            Result += sign * self.matrix[0][focus] * \
                subdeterminant
            
        return Result
    
    def flatten(self):
        self.matrixList = []
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrixList.append(self.matrix[i][j])
        nestedResult = Matrix(1, self.rows * self.columns, 
                              self.matrixList)
        nestedResult.matrix = nestedResult.matrix[0]
        return nestedResult
    
if __name__ == "__main__":
    print("Test the Matrix class")
    myMatrix = Matrix(2, 3)
    print(myMatrix.rows)
    print(myMatrix.columns)
    print(myMatrix.matrix, '\n')
    
    z = list(range(6))
    myMatrix2 = Matrix(2, 3, z)
    myMatrix2 += 2
    print(myMatrix2.matrix)
    print("\nPerform scalar and matrix addition")
    myMatrix2 += [[2, 4, 6], [8, 10, 12]]
    print(myMatrix2.matrix)
    print("\nPerform Element-wise product")
    A = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    B = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    print(A.matrix)
    print(B.matrix)
    print((A * B).matrix)
    print("\nDot product")
    Price = Matrix(1, 3, [1, 2, 1])
    Sales = Matrix(3, 5, 
        [5, 3, 4, 3, 2, 2, 3, 3, 4, 4, 1, 2, 4, 2, 3])
    print(Price.matrix)
    print(Sales.matrix)
    print(Price.dot(Sales).matrix)

    print("\nTransposing a matrix")
    print(A.matrix)
    print(A.transpose().matrix)
    [[1, 2, 3], [4, 5, 6]]
    [[1, 4], [2, 5], [3, 6]]
    print("\nCalculating the determinant")
    A = Matrix(2, 2, [1, 2, 3, 4])
    print(A.determinant())
    B = Matrix(3, 3, [2, 5, 1, 5, 6, 7, 10, 9, 8])
    print(B.determinant())
    print("\nFlattening the matrix")
    A = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(A.matrix)
    print(A.flatten().matrix)