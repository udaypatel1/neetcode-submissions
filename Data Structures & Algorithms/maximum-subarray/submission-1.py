class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
        kadanes algo

        2 choices:
            - should we extend the current subarray?
            - should we start a new subarray and kill the running one?
        '''

        memo = dict()

        def dfs(i):

            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]

            # Recurrence relation: extend the previous subarray or start a fresh one at nums[i]
            result = max(nums[i], dfs(i-1) + nums[i])

            memo[i] = result

            return result

        # Calculate max(dp(i)) across all possible ending indices from 0 to n-1
        return max(dfs(i) for i in range(len(nums)))
