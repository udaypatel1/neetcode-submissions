class Solution:

    def can_communicate(self, grid, row, col):

        # check row
        for c in range(len(grid[0])):
            if c != col and grid[row][c] == 1:
                return True

        # check column
        for r in range(len(grid)):
            if r != row and grid[r][col] == 1:
                return True

        return False

    def countServers(self, grid: List[List[int]]) -> int:

        total = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1 and self.can_communicate(grid, row, col):
                    total += 1
        
        return total