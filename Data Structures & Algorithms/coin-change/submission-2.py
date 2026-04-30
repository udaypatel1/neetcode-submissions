class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(remaining):

            if remaining == 0:
                return 0  # 0 coins needed

            if remaining < 0:
                return float('inf')  # invalid path

            if remaining in memo:
                return memo[remaining]
            
            ways = float('inf')
            for coin in coins:
                ways = min(ways, 1 + dfs(remaining - coin))
            
            memo[remaining] = ways

            return ways
            
        ans = dfs(amount)

        return ans if ans != float('inf') else -1
        