from collections import deque

class Solution:

    def _bfs(self, grid, row, col, visited, dirs):

        q = deque([(row, col)])

        visited.add((row, col))

        while q:

            cur_row, cur_col = q.pop()

            for d_row, d_col in dirs:
                
                n_row = cur_row + d_row
                n_col = cur_col + d_col

                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):

                    if grid[n_row][n_col] == '1' and (n_row, n_col) not in visited:

                        q.append((n_row, n_col))
                        visited.add((n_row, n_col))

    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()

        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == '1' and (row, col) not in visited:

                    self._bfs(grid, row, col, visited, dirs)
                    num_islands += 1
        
        return num_islands
                
    
        