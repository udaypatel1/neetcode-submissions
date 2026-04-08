from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        '''
        multi source BFS problem

        1. fill the queue with all treasure chest locations
        2. start multi source BFS from these chests, with traversal rules
        3. need to keep track of a given chests reachable lands
        '''

        # fill our queue with starters

        q = deque()
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                # if chest, add to queue
                if grid[row][col] == 0:
                    
                    # (row, col, epoch)
                    q.append((row, col, 0))
                    visited.add((row, col))


        # start multi source after queue is filled

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

                    # if land, add to queue
                    if grid[n_row][n_col] == 2147483647 and (n_row, n_col) not in visited:

                        visited.add((n_row, n_col))

                        new_epoch = epoch + 1

                        grid[n_row][n_col] = new_epoch

                        q.append((n_row, n_col, new_epoch))