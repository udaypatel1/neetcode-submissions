class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # collect rottens in queue

        NUM_FRESH_FRUITS = 0

        q = collections.deque()

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 2:
                    q.append((row, col, 0))

                if grid[row][col] == 1:
                    NUM_FRESH_FRUITS += 1

        
        # multi source BFS

        dirs = {
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        }

        visited = set()
        max_epoch = 0

        while q:

            c_row, c_col, c_epoch = q.popleft()

            # cardinal directions
            for d_row, d_col in dirs:

                n_row = d_row + c_row
                n_col = d_col + c_col

                # boundary check
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):
                    
                    # visited check
                    if (n_row, n_col) not in visited:

                        # is fresh fruit check
                        if grid[n_row][n_col] == 1:

                            NUM_FRESH_FRUITS -= 1

                            n_epoch = c_epoch + 1

                            q.append((n_row, n_col, n_epoch))
                            max_epoch = max(n_epoch, max_epoch)
                            visited.add((n_row, n_col))
        
        if NUM_FRESH_FRUITS != 0:
            return -1
        
        return max_epoch



            
        