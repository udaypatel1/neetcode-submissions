class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(cur_house_idx):

            if cur_house_idx == len(nums):
                return 0

            if cur_house_idx > len(nums):
                return 0

            if cur_house_idx in memo:
                return memo[cur_house_idx]

            # recursive case

            # two options -> take money, skip next house OR dont take money, go to next house
            # and i want the max money from those two options

            ways = max(
                nums[cur_house_idx] + dfs(cur_house_idx + 2),
                dfs(cur_house_idx + 1)
            )

            memo[cur_house_idx] = ways

            return ways

        return dfs(0)




        