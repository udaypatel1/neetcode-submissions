class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        '''
        LIS ending at idx or LIS starting at idx?
        '''

        memo = {}

        def dfs(idx, prev_idx):

            if (idx, prev_idx) in memo:
                return memo[(idx, prev_idx)]

            # base case
            if idx >= len(nums):
                return 0

            # skip current number
            skip = dfs(idx + 1, prev_idx)

            # take current number if valid
            take = 0
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                take = 1 + dfs(idx + 1, idx)

            result = max(skip, take)

            memo[(idx, prev_idx)] = result
            return result

        return dfs(0, -1)

