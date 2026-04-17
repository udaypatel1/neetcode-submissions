class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = dict()

        def dfs(index):
            
            # memo check
            if index in memo:
                return memo[index]
            
            # 1. base case
            if index >= len(nums):
                return 0
            
            # 2. recursive case
            '''
            max money from robbing cur house and skipping the next (index + 2)
            
            OR

            don't take the money from cur house and go to the next house -> dfs(index + 1)
            '''
            ways = max(
                nums[index] + dfs(index + 2),
                dfs(index + 1)
            )


            # update memo
            memo[index] = ways

            return ways

        return dfs(0)
        
        


        