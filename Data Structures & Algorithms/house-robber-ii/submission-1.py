class Solution:

    def dfs(self, nums):

        memo = {}

        def recurse(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            # take or skip
            res = max(
                nums[i] + recurse(i + 2),
                recurse(i + 1)
            )

            memo[i] = res
            return res

        return recurse(0)

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # excluse first house, exclude last house, get max of both runs

        return max(
            self.dfs(nums[1:]),
            self.dfs(nums[:-1])
        )