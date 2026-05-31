class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        '''
        The following works, but will TLE because of runtime complexity.
        Need to optimize.

        #########
        LEN_S = len(s)

        memo = dict()

        def dfs(idx):

            if idx in memo:
                return memo[idx]

            if s[idx] != '0':
                return False

            if idx == LEN_S - 1:
                return True

            if idx >= LEN_S:
                return False

            for j in range(idx + 1, LEN_S):

                if (idx + minJump <= j <= min(idx + maxJump, LEN_S - 1)) and s[j] == '0':

                    result = dfs(j)

                    if result:
                        memo[idx] = result
                        return True
            
            memo[idx] = False
            return False
        
        return dfs(0)

        #####
        Option 2: Still TLE but tighter search space

        LEN_S = len(s)

        memo = dict()

        def dfs(idx):

            if idx in memo:
                return memo[idx]
            
            if idx >= LEN_S:
                return False
            
            if idx == LEN_S - 1:
                return True

            if s[idx] != '0':
                return False
            
            # Notice how we optimized the loop to tighten the search space
            for j in range(
                idx + minJump,
                min(idx + maxJump + 1, LEN_S)
            ):

                if s[j] == '0' and dfs(j):

                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return False
        
        return dfs(0)
        ###
        '''

        n = len(s)

        q = collections.deque([0])
        visited = {0}

        farthest = 0

        while q:

            i = q.popleft()

            if i == n - 1:
                return True

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0' and j not in visited:
                    visited.add(j)
                    q.append(j)

            farthest = max(farthest, end)

        return False
            
        
                    

        