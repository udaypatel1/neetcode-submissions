class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        my state is (row, col)
        '''

        memo = {}

        def dfs(row, col):

            # check memo first
            if (row, col) in memo:
                return memo[(row, col)]

            # 1. Base Case
            if row == m - 1 and col == n - 1:
                # we've reached the end state
                return 1

            # 2. Recursive Case

            ways = 0

            dirs = [
                (1,0),
                (0,1),
            ]

            for d_row, d_col in dirs:

                n_row = d_row + row
                n_col = d_col + col

                # boundary check
                if n_row >= 0 and n_row < m and n_col >= 0 and n_col < n:

                    # increment on ways
                    ways += dfs(n_row, n_col)

                    # update memo
                    memo[row, col] = ways

            return ways

        return dfs(0,0)
                    

            


        