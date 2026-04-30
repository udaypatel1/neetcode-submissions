class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(remaining):

            if remaining in memo:
                return memo[remaining]

            if remaining == 0:
                return 1
            
            if remaining < 0:
                return 0
            
            ways = 0

            ways = dfs(remaining - 1) + dfs(remaining - 2)

            memo[remaining] = ways

            return ways

        return dfs(n)


        