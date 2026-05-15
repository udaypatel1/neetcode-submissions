from collections import defaultdict, deque

class Solution:

    def dfs(self, key, adj, visited):

        st = deque([key])

        while st:

            k = st.pop()
            visited.add(k)

            children = adj[k]

            for child in children:
                if child not in visited:
                    st.append(child)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adj = defaultdict(set)

        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):

                if isConnected[row][col] == 1:
                    adj[row].add(col)
                    adj[col].add(row)
        
        '''
        run DFS on each key in adj
        track how many unique DFS are possible in the adj
        thats how many provinces exist
        '''

        visited = set()
        num_provinces = 0

        for key in adj:

            if key not in visited:
                self.dfs(key, adj, visited)
                num_provinces += 1
        
        return num_provinces



        
        


            