class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = dict()

        def dfs(cur_coin_idx, remaining):

            # check memo
            if (cur_coin_idx, remaining) in memo:
                return memo[(cur_coin_idx, remaining)]

            # base case
            if remaining == 0:
                return 0
            
            if remaining < 0 or cur_coin_idx < 0:
                return float('inf')

            # option 1: use the coin and decrement, stay at the same coin
            take = 1 + dfs(cur_coin_idx, remaining - coins[cur_coin_idx])

            # option 2: don't take the coin, don't decrement, just move on
            skip = dfs(cur_coin_idx - 1, remaining)

            minimum_steps = min(take, skip)

            # update memo
            memo[(cur_coin_idx, remaining)] = minimum_steps

            # we take the min value of either the skip or take step
            return minimum_steps

        res = dfs(len(coins) - 1, amount)
        
        return res if res != float('inf') else -1
            