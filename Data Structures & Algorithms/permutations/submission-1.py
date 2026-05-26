class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        used = set()

        def dfs(path):

            if len(used) == len(nums):
                # we have 1 permutation, used up all nums
                result.append(path[:])
                return

            for num in nums:

                if num in used:
                    continue
                
                # add to path
                used.add(num)
                path.append(num)

                # do
                dfs(path)

                # undo
                path.pop()
                used.remove(num)

        dfs([])

        return result
        