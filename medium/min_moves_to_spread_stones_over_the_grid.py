from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        def get_min_move(i, j):
            shortest = 10
            k, l = 0, 0
            for r in range(3):
                for c in range(3):
                    if grid[r][c] > 1:
                        if shortest > abs(r-i) + abs(c-j):
                            shortest = abs(r-i) + abs(c-j)
                            k, l = r, c
            return [shortest,k,l]
        
        def is_grid_final():
            for i in range(3):
                for j in range(3):
                    if grid[i][j] != 1:
                        return False
            return True
        
        shortest_moves = 0
        while not is_grid_final():
            tem_min = 100
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 0:
                        _min_move, k, l = get_min_move(i, j)
                        print(f"k: {k}, l: {l}")
                        tem_min = min(tem_min, _min_move)
            # print(f"first tem min: {tem_min}")
            flag = False
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 0:
                        _min_move, k, l = get_min_move(i, j)
                        if tem_min == _min_move :
                            shortest_moves += _min_move
                            grid[k][l] -= 1
                            grid[i][j] = 1
                            flag = True
                    if flag :
                        break
                if flag:
                    break
            # break
        
        return shortest_moves
    
sol = Solution()
grid = [[1,1,0],[1,1,1],[1,2,1]]
grid = [[1,3,0],[1,0,0],[1,0,3]]
print(sol.minimumMoves(grid))
