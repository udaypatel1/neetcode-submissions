
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        memo = dict()

        def dfs(ptr_s, ptr_t):

            if (ptr_s, ptr_t) in memo:
                return memo[(ptr_s, ptr_t)]

            # matched all of s
            if ptr_s >= len(s):
                return True

            # ran out of t first
            if ptr_t >= len(t):
                return False

            if s[ptr_s] == t[ptr_t]:
                result = dfs(ptr_s + 1, ptr_t + 1)
            else:
                result = dfs(ptr_s, ptr_t + 1)

            memo[(ptr_s, ptr_t)] = result

            return result

        return dfs(0,0)



        


        