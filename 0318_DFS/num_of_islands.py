import sys

class Solution:
    def dfs(self, i, j):
        if i < 0 or i >= self.n_row or j < 0 or j >= self.n_col or self.grid[i][j] == '1':
            return

        self.grid[i][j] = '2'
        self.dfs(i-1, j)  # down
        self.dfs(i+1, j)  # up
        self.dfs(i, j-1)  # left
        self.dfs(i, j+1)  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        n_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    n_island += 1
        return n_island