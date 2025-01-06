from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        tracking = [['x' for _ in range(len(grid[0]))] for _ in range(len(grid))]
        fishes = []
        m, n = len(grid), len(grid[0])
        def bfs(i,j, cur_fishes):

            if i==m or i==-1 or j==n or j==-1 or tracking[i][j] != 'x':
                return
            print("\n\ni,j =",i,j, " - cur_fishes:", cur_fishes)
            tracking[i][j] = 'v'
            for row in tracking:
                print(row)
            
            f1,f2,f3,f4 = 0,0,0,0

            if (i-1 >= 0 and (tracking[i-1][j] == 'v' or grid[i-1][j] == 0 )) or i== 0:
                f1 = 1
            else:
                bfs(i-1, j, cur_fishes+grid[i][j])
            
            if (j-1 >= 0 and (tracking[i][j-1] == 'v' or grid[i][j-1] == 0 )) or j== 0:
                f2 = 1
            else:
                bfs(i, j-1, cur_fishes+grid[i][j])
            
            if (j+1 < n and (tracking[i][j+1] == 'v' or grid[i][j+1] == 0 )) or j== n-1:
                f3 = 1
            else:
                bfs(i, j+1, cur_fishes+grid[i][j])

            if (i+1 < m and (tracking[i+1][j] == 'v' or grid[i+1][j] == 0 )) or i== m-1:
                f4 = 1
            else:
                bfs(i+1, j, cur_fishes+grid[i][j])

            if f1*f2*f3*f4 :
                fishes.append(cur_fishes)
                if grid[i][j]:
                    fishes[-1]+=grid[i][j]
                    
                bfs(i-1,j,0)
                bfs(i+1,j,0)
                bfs(i,j-1,0)
                bfs(i,j+1,0)

        bfs(0,0,0)
        print(fishes)
        return max(fishes)
    
sol = Solution()
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
grid = [[10,5],[8,0]]
print(sol.findMaxFish(grid))




