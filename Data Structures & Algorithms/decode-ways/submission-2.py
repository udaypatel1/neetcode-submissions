class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = {}

        def dfs(i):

            if i == n:
                return 1  # valid split reached end

            if s[i] == '0':
                return 0  # invalid encoding

            if i in memo:
                return memo[i]

            # take 1 digit
            ways = dfs(i + 1)

            # take 2 digits (if valid)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)