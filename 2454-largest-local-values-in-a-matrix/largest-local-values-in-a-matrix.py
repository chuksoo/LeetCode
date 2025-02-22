class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # n = len(grid)
        # maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        # for i in range(n - 2):
        #     for j in range(n - 2):
        #         max_value = max(
        #             grid[i][j], grid[i][j+1], grid[i][j+2],
        #             grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
        #             grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
        #         )
        #         maxLocal[i][j] = max_value
        # return maxLocal

        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        # iterate over all possible 3x3 submatrics
        for i in range(n - 2):
            for j in range(n - 2):
                # compute max element in 3x3 submatix
                max_element = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_element = max(max_element, grid[x][y])
                maxLocal[i][j] = max_element
        return maxLocal
            