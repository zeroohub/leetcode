# -*- coding: utf-8 -*-
class Solution(object):

    def dfs(self, grid, pos_i, pos_j):
        if grid[pos_i][pos_j] != '1':
            return
        grid[pos_i][pos_j] = '#'
        for pos in [(pos_i - 1, pos_j), (pos_i + 1, pos_j), (pos_i, pos_j - 1), (pos_i, pos_j + 1)]:
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                self.dfs(grid, pos[0], pos[1])

    def numIslands(self, grid):
        """
        DFS works great, with some optimize from network
        :type grid: List[List[str]]
        :rtype: int
        """
        self.count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1
                    self.dfs(grid, i, j)

        return self.count

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
