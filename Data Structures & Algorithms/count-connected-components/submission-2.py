from collections import deque, defaultdict

class Solution:

    def _dfs(self, key, adj, visited):

        st = deque()

        st.append(key)

        visited.add(key)

        while st:

            cur_key = st.pop()

            if adj.get(cur_key):

                for child in adj[cur_key]:
                    if child not in visited:
                        visited.add(child)
                        st.append(child)

        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(set)

        for a, b in edges:

            adj[a].add(b)
            adj[b].add(a)

        '''
        run dfs on each key in adj
        keep track of global visited
        dont run dfs on visited keys

        answer = amount of times we have to run dfs
        '''

        visited = set()
        components = 0

        for key in range(n):

            if key not in visited:
                self._dfs(key, adj, visited)
                components += 1
        
        return components
        
