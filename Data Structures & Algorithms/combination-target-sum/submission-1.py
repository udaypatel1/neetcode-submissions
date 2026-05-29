class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        nums.sort()

        def dfs(start, path, remaining):

            if remaining == 0:
                result.append(path[:])
                return
            
            for j in range(start, len(nums)):

                if j > start and nums[j] == nums[j - 1]:
                    continue
                
                if remaining - nums[j] < 0:
                    return
                
                path.append(nums[j])

                dfs(j, path, remaining - nums[j])

                path.pop()
        
        dfs(0, [], target)

        return result

            
        