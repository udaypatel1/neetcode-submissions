class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return True
            
            if i > len(nums) - 1:
                return False
            
            # recursive case

            for j in range(nums[i], 0, -1):

                if i + j < len(nums) and dfs(i + j):
                    
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)