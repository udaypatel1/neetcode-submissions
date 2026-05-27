class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates = sorted(candidates)

        def dfs(idx, path, remaining):

            # 1. Base Case
            if remaining == 0:
                result.append(path[:])
                return

            # End case Prune
            if idx == len(candidates):
                return

            for j in range(idx, len(candidates)):

                '''
                DEDUPE
                '''
                # This says, if we're above our start idx, and it's the same number we saw prior, just skip
                # This is essentially our "dedup" step, so results doesn't have any duplicates
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue

                '''
                PRUNE
                '''
                # Because we sorted, we know that we can break here, to avoid unnecessary backtracking
                if candidates[j] > remaining:
                    break
            
                # take and do
                path.append(candidates[j])
                dfs(j + 1, path, remaining - candidates[j])

                # undo
                path.pop()

        dfs(0, [], target)

        return result
        