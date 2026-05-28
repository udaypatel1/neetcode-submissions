class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        '''
        in order to dedupe in backtracking, so far as I know,
        we need to sort the original input
        and dedupe in a loop, similar to how permutations II does it

        i dont know of any other way (yet) to dedupe _without_ sorting the input first
        '''

        nums.sort()
        LEN_NUMS = len(nums)

        result = []

        def dfs(index, path):
            
            # append by default
            result.append(path[:])

            for sub_idx in range(index, LEN_NUMS):

                # is the runner num the same as its previous? if so, move on
                if sub_idx > index and nums[sub_idx] == nums[sub_idx - 1]:
                    continue
                
                # add to path
                path.append(nums[sub_idx])

                # move idx and do
                dfs(sub_idx + 1, path)

                # undo
                path.pop()
        
        dfs(0, [])

        return result



