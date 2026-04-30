class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        '''
        i in s1 and j in s2 are my states
        '''

        memo = {}
        
        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0
            
            ways = 0
            if text1[i] == text2[j]:
                ways = 1 + dfs(i + 1, j + 1)
            else:
                # if the two chars arent diff, we do a choice
                # skip or take

                ways = max(
                    dfs(i + 1, j),
                    dfs(i, j + 1)
                )

            memo[(i, j)] = ways
            return ways
        
        return dfs(0, 0)