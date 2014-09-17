class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if row - 1 >= 0 and col - 1 >= 0:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                elif row - 1 >= 0:
                    grid[row][col] += grid[row-1][col] 
                elif col - 1 >= 0:
                    grid[row][col] += grid[row][col-1]

        return grid[-1][-1]

grid = [[1,2],[1,1]]
a = Solution()
print a.minPathSum(grid)