class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = dict()

        def dfs(house_idx):

            if house_idx in memo:
                return memo[house_idx]

            if house_idx > len(nums) - 1:
                return 0
            
            take = nums[house_idx] + dfs(house_idx + 2)
            skip = dfs(house_idx + 1)

            result = max(take, skip)

            memo[house_idx] = result

            return result
        
        return dfs(0)
        