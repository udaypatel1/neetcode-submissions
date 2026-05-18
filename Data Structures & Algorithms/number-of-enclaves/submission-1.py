from collections import deque

class Solution:
    
    def bfs(self, row, col, grid, visited, enclaves):

        is_enclave = False
        total_land = 0

        dirs = [
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]

        q = deque()
        q.append((row, col))

        while q:

            c_row, c_col = q.popleft()
            total_land += 1

            visited.add((c_row, c_col))

            if is_enclave == False and (c_row == 0 or c_row == len(grid) - 1 or c_col == 0 or c_col == len(grid[c_row]) - 1):
                enclaves += 1
                is_enclave = True

            for d_row, d_col in dirs:

                n_row = d_row + c_row
                n_col = d_col + c_col

                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]) and grid[n_row][n_col] == 1 and (n_row, n_col) not in visited:
                    q.append((n_row, n_col))
                    visited.add((n_row, n_col))
        
        return 0 if is_enclave else total_land
        
    def numEnclaves(self, grid: List[List[int]]) -> int:

        '''
        BFS on each unvisited land spot

        for that island, check if it hits some boundary
        if so, mark that land as enclave, increment
        make sure to finish the BFS crawl and add to visited
        '''

        visited = set()
        enclaves = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 1 and (row, col) not in visited:

                    enclaves += self.bfs(row, col, grid, visited, enclaves)

        return enclaves
        