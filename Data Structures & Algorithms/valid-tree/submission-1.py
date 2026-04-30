from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # a valid tree means there isnt a cycle
        # at each iteration, check to see if the tree is valid
        # by making sure a cycle doesnt exist

        '''
        given edges, we want to make sure
        that no child node points to anything but its parent
        a parent can have many children, but a child can only have 1 parent
        multiple parents = cycle
        '''

        '''
        what data structure would help us?

        Note: this is a union find problem that I have not practiced yet
        '''

        # quick check

        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for child in graph[node]:
                if child == parent:
                    continue # don't go back up the tree
            
                if child in visited:
                    return False # cycle detected, immediately
                
                if not dfs(child, node):
                    return False

            return True
        
        # start DFS from node 0
        if not dfs(0, -1):
            return False

        # must be fully connected
        return len(visited) == n

        



        