from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        largest_island = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 1 and (row, col) not in visited:

                    # run dfs
                    stack = deque([(row, col)])
                    visited.add((row, col))

                    directions = [
                        (1,0),
                        (-1,0),
                        (0,1),
                        (0,-1)
                    ]

                    local_island_size = 0

                    while stack:

                        stack_row, stack_col = stack.pop()
                        local_island_size += 1

                        for d_row, d_col in directions:

                            n_row = d_row + stack_row
                            n_col = d_col + stack_col

                            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):

                                if grid[n_row][n_col] == 1 and (n_row, n_col) not in visited:

                                    stack.append((n_row, n_col))
                                    visited.add((n_row, n_col))

                    largest_island = max(largest_island, local_island_size)


        return largest_island


        
        