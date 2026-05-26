class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(index, path, remaining):

            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            if index == len(nums):
                return

            # TAKE current number
            path.append(nums[index])

            dfs(
                index,
                path,
                remaining - nums[index]
            )

            path.pop()

            # SKIP current number
            dfs(
                index + 1,
                path,
                remaining
            )

        dfs(0, [], target)

        return result
            
            
                



        