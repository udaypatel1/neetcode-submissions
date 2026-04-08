from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        all_fresh_fruits = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 2:
                    q.append((row, col, 0))
                
                if grid[row][col] == 1:
                    all_fresh_fruits += 1

        if all_fresh_fruits == 0:
            return 0

        min_minutes = 0

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        while q:

            row, col, epoch = q.popleft()

            for d_row, d_col in directions:

                n_row = d_row + row
                n_col = d_col + col

                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):

                    if grid[n_row][n_col] == 1:

                        grid[n_row][n_col] = 2
                        all_fresh_fruits -= 1
                        
                        new_epoch = epoch + 1

                        q.append((n_row, n_col, new_epoch))

                        min_minutes = max(min_minutes, new_epoch)

        return min_minutes if all_fresh_fruits == 0 else -1




        
        