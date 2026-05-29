class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        # sort because we want to dedupe step later
        nums.sort()

        def dfs(start, path, remaining):

            # base case
            if remaining == 0:
                result.append(path[:])
                return
            
            for j in range(start, len(nums)):

                # dedupe
                if j > start and nums[j] == nums[j - 1]:
                    continue
                
                # early pruning to kill branch if we're under target
                if remaining - nums[j] < 0:
                    return
                
                # take
                path.append(nums[j])

                # do
                dfs(j, path, remaining - nums[j])

                # undo
                path.pop()
        
        dfs(0, [], target)

        return result

            
        