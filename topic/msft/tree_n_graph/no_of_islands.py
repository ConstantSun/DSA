from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n =len(grid), len(grid[0])
        visited =[ [0 for _ in range(n)] for _ in range(m)]
        def dfs(i: int, j: int):
            if i < 0 or j<0 or i>=m or j >= n or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = 1
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    count += 1
                dfs(i, j)
        return count
    
sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))

