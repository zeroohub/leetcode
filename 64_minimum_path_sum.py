# -*- coding: utf-8 -*-
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if col == 0 and row == 0:
                    continue
                elif col == 0:
                    grid[row][col] += grid[row-1][col]

                elif row == 0:
                    grid[row][col] += grid[row][col-1]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])

        return grid[-1][-1]

print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
