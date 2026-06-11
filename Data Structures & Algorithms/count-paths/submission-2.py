class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dirs = [
            (0,1),
            (1,0),
        ]

        memo = dict()

        def dfs(row, col):

            if (row, col) in memo:
                return memo[(row, col)]

            # base case
            if row == m - 1 and col == n - 1:
                return 1

            

            # recursive case
            ways = 0
            for d_row, d_col in dirs:

                n_row = d_row + row
                n_col = d_col + col

                # boundary check
                if 0 <= n_row < m and 0 <= n_col < n:

                    ways += dfs(n_row, n_col)
            
                    memo[(row, col)] = ways

            return ways
    
        return dfs(0,0)




        