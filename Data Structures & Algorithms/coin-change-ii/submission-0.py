class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = dict()

        def dfs(coin_idx, remaining):

            if (coin_idx, remaining) in memo:
                return memo[(coin_idx, remaining)]

            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            if coin_idx >= len(coins):
                return 0
            
            # take current coin or skip it

            take = dfs(coin_idx, remaining - coins[coin_idx])
            skip = dfs(coin_idx + 1, remaining)

            result = take + skip

            memo[(coin_idx, remaining)] = result

            return result

        return dfs(0, amount)
        


        
        