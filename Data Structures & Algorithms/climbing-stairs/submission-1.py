class Solution:
    def climbStairs(self, n: int) -> int:

        memo = dict()

        def dfs(number_of_stairs_left):

            if number_of_stairs_left in memo:
                return memo[number_of_stairs_left]

            # 1. base case
            if number_of_stairs_left == 0:
                return 1
            if number_of_stairs_left < 0:
                return 0
            
            # 2. recursive case
            ways = dfs(number_of_stairs_left - 1) + dfs(number_of_stairs_left - 2)

            memo[number_of_stairs_left] = ways
            
            return ways

        return dfs(n)

        