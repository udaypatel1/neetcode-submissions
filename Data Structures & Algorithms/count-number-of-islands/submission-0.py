from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == '1' and (row, col) not in visited:

                    stack = deque([(row, col)])
                    visited.add((row, col))

                    directions = [
                        (-1,0),
                        (1,0),
                        (0,1),
                        (0,-1)
                    ]

                    while stack:

                        row, col = stack.pop()

                        for d_row, d_col in directions:

                            n_row = d_row + row
                            n_col = d_col + col

                            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):

                                if grid[n_row][n_col] == '1' and (n_row, n_col) not in visited:

                                    stack.append((n_row, n_col))
                                    visited.add((n_row, n_col))

                    num_islands += 1

        return num_islands



        