class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        '''
        at each char, we can either do 3 things to it

        base case is when manipulated str word1 == word2, return

        i == ptr word 1
        j == ptr word 2
        '''

        memo = dict()

        def dfs(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:

                result = dfs(i + 1, j + 1)

                memo[(i, j)] = result

                return result

            # 3 choices

            insert = dfs(i, j + 1)
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)

            result = 1 + min(
                insert,
                delete,
                replace
            )

            memo[(i, j)] = result

            return result
        
        return dfs(0,0)

                
                

            