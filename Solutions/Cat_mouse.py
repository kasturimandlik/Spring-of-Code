
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        mouse_pos = cat_pos = None
        available = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    available += 1
                if grid[i][j] == 'M':
                    mouse_pos = (i, j)
                elif grid[i][j] == 'C':
                    cat_pos = (i, j)
        
        @functools.lru_cache(None)
        def dp(turn, mouse_pos, cat_pos):
            if turn == available * 2:
                return False
            if turn % 2 == 0:
                i, j = mouse_pos
                for di, dj in dirs:
                    for jump in range(mouseJump + 1):
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            if dp(turn + 1, (new_i, new_j), cat_pos) or grid[new_i][new_j] == 'F':
                                return True
                        else:
                            break
                return False
            else:
                i, j = cat_pos
                for di, dj in dirs:
                    for jump in range(catJump + 1):
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            if not dp(turn + 1, mouse_pos, (new_i, new_j)) or (new_i, new_j) == mouse_pos or grid[new_i][new_j] == 'F':
                                return False
                        else:
                            break
                return True

        return dp(0, mouse_pos, cat_pos)
