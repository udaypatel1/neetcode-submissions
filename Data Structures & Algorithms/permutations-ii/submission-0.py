class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        '''
        ok so for permutations, we need to keep track of a 'used' set, as to not repeat
        also for dedupe, the only way I know how, is to sort the input array
        '''

        nums.sort()

        result = []
        used = set()

        def dfs(path):
            
            # Base Case
            '''
            Only append to result when our path is same length as nums
            '''
            if len(path) == len(nums):
                result.append(path[:])
                return


            for i in range(len(nums)):

                # Skip if we've already used this index
                if i in used:
                    continue

                # Key statement; this is the DEDUPE step here
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in used:
                    continue

                # take
                used.add(i)
                path.append(nums[i])

                # do
                dfs(path)

                # undo
                path.pop()
                used.remove(i)

        # notice only the path is given as argument
        dfs([])

        return result


        
        