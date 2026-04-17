class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = dict()

        def dfs(index, current_sum):

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            if index == len(nums):

                if current_sum == target:
                    return 1
                else:
                    return 0
            
            ways = dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])

            return ways

        return dfs(0, 0)
        