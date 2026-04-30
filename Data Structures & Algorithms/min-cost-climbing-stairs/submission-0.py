class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        n = len(cost)

        def dfs(i):

            # i = min cost to reach the top

            # base case
            if i == n:
                return 0
            if i > n:
                return 0
            
            if i in memo:
                return memo[i]
            
            # recursive case

            cur_cost = cost[i] + min(dfs(i + 1), dfs(i + 2))

            memo[i] = cur_cost

            return cur_cost

        return min(dfs(0), dfs(1))