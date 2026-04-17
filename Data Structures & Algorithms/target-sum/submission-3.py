class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = dict()

        def dfs(index, current_sum):

            # 1. Check Memo / Cache is pre-computed state exists
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # 2. Base Case / when we should stop
            if index == len(nums):

                if current_sum == target:
                    return 1
                else:
                    return 0
            
            # 3. Recursive Case
            ways = dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])

            # 4. Update memo / cache / stored state with new value
            memo[(index, current_sum)] = ways
            
            return ways

        return dfs(0, 0)
        