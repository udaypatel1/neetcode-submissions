class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
        backtracking

        format:

            define state (some_state, existing_path)

            check if complete -> add to result and return

            for choice in choices:
                make the choice
                dfs over it
                undo that choice from path
            
        return result

        choices for this problem:
            either take the current number, or skip it
        '''

        result = []

        def dfs(index, path):

            # 1. base case / completion
            if index == len(nums):
                result.append(path[:])
                return

            # 2. backtrack over choices we have

            # take current
            path.append(nums[index])

            dfs(index + 1, path)

            # undo that
            path.pop()

            # -------
            # skip

            dfs(index + 1, path)

        dfs(0, [])

        return result


        